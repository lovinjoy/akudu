#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Client, also as Proxy.
"""
__author__ = 'Zagfai'
__date__ = '2023-03'

import asyncio

from . import connection
from . import negotiate


class Client:

    def __init__(self, host, port,
            # TODO 
            reconnect = False,  # Raise error if connection was broken or reconnect
            connect_timeout = None,
            read_timeout = None,
            write_timeout = None,
            ssl = None,

            wait_size = 10,  # Max waiting size of messages sent but not reply
            wait_timeout = 60,  # Seconds waiting for reply or raise Error
            negotiate_method=negotiate.SASL_Plain):

        self.host = host
        self.port = port
        self.wait_size = wait_size
        self.wait_timeout = wait_timeout
        self.negotiate_method = negotiate_method


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

    async def close(self):
        await self._conn.close()
        self._conn = None
