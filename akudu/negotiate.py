#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Negotators
"""
__author__ = 'Zagfai'
__date__ = '2023-03'

import logging

from .kudu.rpc.rpc_header_pb2 import RequestHeader
from .kudu.rpc.rpc_header_pb2 import ResponseHeader
from .kudu.rpc.rpc_header_pb2 import NegotiatePB
from .kudu.rpc.rpc_header_pb2 import AuthenticationTypePB
from .kudu.rpc.rpc_header_pb2 import ConnectionContextPB

from .message import Message

logger = logging.getLogger(__name__)


class SASL_Plain:
    """SASL Plain Negotate without TLS, the base way to connect."""

    def __init__(self, conn):
        self._conn = conn

    async def negotiate(self, reader, writer):

        # connection header
        writer.write(b'hrpc\x09\x00\x00')

        # negotiate
        header_pb = RequestHeader(call_id=-33)
        body_pb = NegotiatePB(step=1)
        writer.write(Message(header_pb, body_pb).serialize())

        resp_msg = await Message().load_from_stream(reader)
        resp_msg.parse(NegotiatePB)
        logging.debug(f'Negotiate received: {resp_msg}')

        # sasl init
        header_pb = RequestHeader(call_id=-33)
        body_pb = NegotiatePB(
                step=2,
                authn_types=[AuthenticationTypePB(sasl={})],
                sasl_mechanisms=[NegotiatePB.SaslMechanism(mechanism='PLAIN')],
                token=b'\x00kudu\x00')
        writer.write(Message(header_pb, body_pb).serialize())

        resp_msg = await Message().load_from_stream(reader)
        resp_msg.parse(NegotiatePB)
        logging.debug(f'SASL init received: {resp_msg}')

        # Connection Context
        header_pb = RequestHeader(call_id=-3)
        body_pb = ConnectionContextPB()
        writer.write(Message(header_pb, body_pb).serialize())

        logging.info("Negotiate Finished with SASL Plain")
