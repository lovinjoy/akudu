#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Client, also as Proxy.
"""
__author__ = 'Zagfai'
__date__ = '2023-03'

import asyncio
import logging

from . import connection
from . import negotiate

from akudu.kudu.master.master_pb2 import ListTablesRequestPB
from akudu.kudu.master.master_pb2 import ListTablesResponsePB

logger = logging.getLogger(__name__)


class Client:

    def __init__(self, host, port,
            # TODO 
            reconnect = False,  # Raise error if connection was broken or reconnect
            connect_timeout = None,
            ssl = None,

            wait_size = 10,  # Max waiting size of messages sent but not reply, or operation would wait for
            wait_timeout = 60,  # Seconds waiting to send msg or for reply, otherwise raise Error
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

    def auto_connect(func):
        async def wrapped_func(self, *args, **kwargs):
            need_disconnect = False
            if not self._conn:
                logger.debug("No connection, auto connect...")
                need_disconnect = True
                await self.connect()
            res = await func(self, *args, **kwargs)
            if need_disconnect:
                logger.debug("Disconnect.")
                await self.close()

            return res

        return wrapped_func

    @auto_connect
    async def list_tables(self):
        service = "kudu.master.MasterService"
        method = "ListTables"
        body = ListTablesRequestPB()
        rep_msg = await self._conn.messenger.call(service, method, body)
        rep_msg.parse(ListTablesResponsePB)
        return rep_msg
