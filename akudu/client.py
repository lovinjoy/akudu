#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Client, also as Proxy.
"""
__author__ = 'Zagfai'
__date__ = '2023-03'

import asyncio

from . import connection


class Client:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._conn = None

    @property
    def connection(self):
        if not self._conn:
            self._conn = connection.Connection(self)
        return self._conn

    async def connect(self):
        if not self._conn:
            self._conn = connection.Connection(self)
        return await self._conn.connect()


    def close(self):
        self._conn = None
