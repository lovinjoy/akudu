#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Message of Wire Protocol, the base message framing for communicating with server.
"""
__author__ = 'Zagfai'
__date__ = '2023-03'

import io
import logging

from . import utils

from .kudu.rpc.rpc_header_pb2 import RequestHeader
from .kudu.rpc.rpc_header_pb2 import ResponseHeader
from .kudu.rpc.rpc_header_pb2 import ErrorStatusPB

logger = logging.getLogger(__name__)

class Message:
    """Message Frame"""

    def __init__(self, header_pb=None, body_pb=None):
        self.header : RequestHeader or ResponseHeader  = header_pb
        self.body : "google.protobuf.message.Message" = body_pb
        self.is_parsed = True
        self.buf = ""

    def __str__(self):
        return f"<akudu.Message: {str(self.header)} body: {str(self.body)}>".replace('\n',' ')

    def serialize(self):
        buf = b''

        header = self.header.SerializeToString()
        header = utils.varint_encode(self.header.ByteSize()) + header

        body = self.body.SerializeToString()
        body = utils.varint_encode(self.body.ByteSize()) + body

        buf = header_size_to_bytes(len(header + body)) + header + body
        logger.debug(f'Request: {header}, {body}')

        self.buf = buf
        return buf

    def parse(self, response_pb_type=None, message_bytes=b""):
        if not self.buf and not message_bytes:
            raise ValueError("Empty message buffer for parse or no input message_bytes.")
        if message_bytes:
            self.buf = message_bytes

        buffer = io.BytesIO(self.buf)

        total_size = buffer.read(4)

        header_size = utils.varint_decode_stream(buffer)
        self.header = ResponseHeader.FromString(buffer.read(header_size))

        body_size = utils.varint_decode_stream(buffer)
        if self.header.is_error:
            self.body = ErrorStatusPB.FromString(buffer.read(body_size))
        elif response_pb_type:
            self.body = response_pb_type.FromString(buffer.read(body_size))

        self.is_parsed = True
        return self

    async def load_from_stream(self, stream_reader):
        """Message from server is not fix length, need reader to read exactly one Message."""

        # Read exactly 4 bytes to indicate Message size
        message_size_bytes = await stream_reader.readexactly(4)
        message_size = int.from_bytes(message_size_bytes, 'big')

        buf = await stream_reader.readexactly(message_size)
        self.buf = message_size_bytes + buf

        buffer = io.BytesIO(buf)
        header_size = utils.varint_decode_stream(buffer)
        self.header = ResponseHeader.FromString(buffer.read(header_size))

        self.is_parsed = False
        return self

def header_size_to_bytes(size):
    return size.to_bytes(4, 'big')
