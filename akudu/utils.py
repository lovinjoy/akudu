#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Utils.
Code here should not import from other modules.
"""
__author__ = 'Zagfai'
__date__ = '2023-03'

import io


def varint_encode(i):
    """Make varint bytes"""
    buf = b''
    while True:
        b = i & 0x7f
        i >>= 7
        if i:
            buf += (b | 0x80).to_bytes(1, 'big')
        else:
            buf += b.to_bytes(1, 'big')
            break
    return buf

def varint_decode_stream(stream):
    """Read a varint from `stream`"""
    shift = 0
    result = 0
    while True:
        b = int.from_bytes(stream.read(1), 'big')
        result |= (b & 0x7f) << shift
        shift += 7
        if not (b & 0x80):
            break

    return result

def varint_decode(bytestring):
    return varint_decode_stream(io.BytesIO(bytestring))


# easy test
if __name__ == "__main__":
    print(varint_encode(0))
    print(varint_decode(varint_encode(0)))

    print(varint_encode(1))
    print(varint_decode(varint_encode(1)))

    print(varint_encode(8))
    print(varint_decode(varint_encode(8)))

    print(varint_encode(10))
    print(varint_decode(varint_encode(10)))

    print(varint_encode(100))
    print(varint_decode(varint_encode(100)))

    print(varint_encode(192))
    print(varint_decode(varint_encode(192)))

    print(varint_encode(65535))
    print(varint_decode(varint_encode(65535)))

    print(varint_encode(65536))
    print(varint_decode(varint_encode(65536)))

    print(varint_encode(9999965536))
    print(varint_decode(varint_encode(9999965536)))
