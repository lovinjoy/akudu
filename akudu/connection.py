#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Service Class, pack up services.
"""
__author__ = 'Zagfai'
__date__ = '2023-03'

import logging
import asyncio

from .messenger import Messenger

from .kudu.server.server_base_pb2 import GetStatusRequestPB
from .kudu.server.server_base_pb2 import GetStatusResponsePB

logger = logging.getLogger(__name__)

class Connection:
    def __init__(self, client):
        self._client = client
        self._negotiator = client.negotiate_method(self)
        self._reader = None
        self._writer = None
        self._connected = False

        self.messenger = None

    async def _connect(self):
        """Connect and negotiate to steady state."""
        self._reader, self._writer = await asyncio.open_connection(self._client.host, self._client.port)
        await self._negotiator.negotiate(self._reader, self._writer)
        self.messenger = Messenger(self, self._client.wait_size, self._client.wait_timeout)
        self._connected = True

    async def connect(self):
        await self._connect()
        return self

    async def close(self):
        self._client._conn = None
        await self.messenger.retire()
        self._writer.close()
        await self._writer.wait_closed()
        logger.debug("Akudu connection closed.")

    async def _keepalive(self):
        # TODO intermittently send and check receive, auto reconnect
        pass

    async def _reconnect(self):
        # TODO
        pass

    async def status(self):
        service = "kudu.server.GenericService"
        method = "GetStatus"
        request = GetStatusRequestPB()
        rep_msg = await self.messenger.call(service, method, request)
        rep_msg.parse(GetStatusResponsePB)
        return rep_msg

    async def __aenter__(self):
        await self._connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            raise
        await self.close()
