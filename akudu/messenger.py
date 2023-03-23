#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Messenger Module, control call-ids, send and receive message, keep messages in single connection.
"""
__author__ = 'Zagfai'
__date__ = '2023-03'

import logging
import asyncio

from .message import Message
from .kudu.rpc.rpc_header_pb2 import RequestHeader
from .kudu.rpc.rpc_header_pb2 import RemoteMethodPB

logger = logging.getLogger(__name__)


class ReceiveError(Exception):
    pass


class Messenger:

    def __init__(self, connection, wait_size=10, wait_timeout=60):
        self._conn = connection
        self._wait_size = wait_size
        self._wait_timeout = wait_timeout

        self._reader = self._conn._reader
        self._writer = self._conn._writer

        self._send_queue = asyncio.Queue(wait_size)

        self._wait_reply = dict()
        self._reply = dict()

        self._sender_task = asyncio.create_task(self._sender())
        self._receiver_task = asyncio.create_task(self._receiver())

        # Call-id is strictly increasing, promise by Messenger
        self.__call_id = 0

    async def _sender(self):
        while True:
            to_send_raw_msg = await self._send_queue.get()
            if not to_send_raw_msg:
                break
            self._writer.write(to_send_raw_msg)
            await self._writer.drain()

    async def _receiver(self):
        while True:
            try:
                msg = await Message().load_from_stream(self._reader)
            except asyncio.exceptions.IncompleteReadError as e:
                logger.debug(f"Stop receiving. Replied left: {len(self._reply)}")
                break
            self._reply[msg.header.call_id] = msg
            self._wait_reply[msg.header.call_id].set()

    async def call(self, service, method, request):
        """ Call Kudu service function.
        raise asyncio.TimeoutError when sender queue full,
        raise akudu.messenger.ReceiveError when NO response from kudu server."""
        self.__call_id += 1
        call_id = self.__call_id

        remote = RemoteMethodPB(service_name=service, method_name=method)
        header = RequestHeader(call_id=call_id, remote_method=remote)
        msg_raw = Message(header, request).serialize()

        await asyncio.wait_for(self._send_queue.put(msg_raw), timeout=self._wait_timeout)

        event = asyncio.Event()
        self._wait_reply[call_id] = event
        await asyncio.wait_for(event.wait(), timeout=self._wait_timeout)  # the second wait
        # TODO should clear up reply or not if timeout?
        try:
            rep = self._reply[call_id]
            del self._reply[call_id]
        except KeyError:
            raise ReceiveError("Call do not reply before connection closed.")

        return rep

    async def retire(self):
        await self._send_queue.put(None)  # end up the sender
        logger.debug("Messenger Retired.")
