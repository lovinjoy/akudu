#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Messenger Module, control call-ids, build message, keep messages in single connection.
"""
__author__ = 'Zagfai'
__date__ = '2023-03'


from .message import Message
from .kudu.rpc.rpc_header_pb2 import RequestHeader
from .kudu.rpc.rpc_header_pb2 import RemoteMethodPB


class Messenger:

    def __init__(self, connection, wait_size=10, wait_timeout=60):
        self._conn = connection
        self.wait_size = wait_size
        self.wait_timeout = wait_timeout

        self._reader = self._conn._reader
        self._writer = self._conn._writer

        # Call-id is strictly increasing, promise by Messenger
        self.__call_id = 0

    async def call(self, service, method, request):
        # TODO here only implement one single call and reply now for test
        remote = RemoteMethodPB(service_name=service, method_name=method)
        header = RequestHeader(call_id=0, remote_method=remote)
        body = request
        self._writer.write(Message(header, body).serialize())

        rep = await Message().load_from_stream(self._reader)
        return rep
