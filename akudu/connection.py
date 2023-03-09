#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Service Class, pack up services.
"""
__author__ = 'Zagfai'
__date__ = '2023-03'

import asyncio


class Connection:
    def __init__(self, client):
        self._client = client
        self._reader = None
        self._writer = None
        self._connected = False

    async def _connect(self):
        self._reader, self._writer = await asyncio.open_connection(self._client.host, self._client.port)
        self._connected = True

    async def connect(self):
        await self._connect()
        return self

    async def close(self):
        # TODO finish message-queues and callbacks
        self._writer.close()
        self._reader.close()
        self._client.close()

    async def __aenter__(self):
        await self._connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            raise
        await self.close()
