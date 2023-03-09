#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Wire Protocol, the base message framing for communicating with server.
"""
__author__ = 'Zagfai'
__date__ = '2023-03'


class Wire:

    def read_varint32():
        pass

    def write_varint32():
        pass

    def call_req(header_pb, body_pb):
        buf = b''

        header = header_pb.SerializeToString()
        header_o = output_stream.OutputStream()
        header_o.AppendVarint32(header_pb.ByteSize())
        header = header_o.ToString() + header

        body = body_pb.SerializeToString()
        body_o = output_stream.OutputStream()
        body_o.AppendVarint32(body_pb.ByteSize())
        body = body_o.ToString() + body

        total_byte_size = len(header + body)
        buf = total_byte_size.to_bytes(4, 'big') + header + body
        print('Request:', header, body)
        return buf


    def extra_resp(resp_bytes, body_pb=NegotiatePB):
        message_size = int.from_bytes(resp_bytes[:4], 'big')

        header_i = input_stream.InputStreamArray(resp_bytes[4:])
        header_size = header_i.ReadVarint32()
        header_data_start_pos = 4 + header_i.Position()

        body_i = input_stream.InputStreamArray(resp_bytes[header_data_start_pos + header_size:])
        body_size = body_i.ReadVarint32()
        body_data_start_pos = header_data_start_pos + header_size + body_i.Position()
        body = resp_bytes[body_data_start_pos: body_data_start_pos+body_size]

        resp_head = ResponseHeader.FromString(resp_bytes[header_data_start_pos: header_data_start_pos+header_size])

        print('--------- Resp Header ----------')
        print(resp_head)

        if resp_head.is_error:
            resp_body = ErrorStatusPB.FromString(body)
        else:
            resp_body = body_pb.FromString(body)

        print('---------- Resp Body -----------')
        print(resp_body)
