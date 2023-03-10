#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Tester
"""
__author__ = 'Zagfai'
__date__ = '2023-03'

import logging
import asyncio
import akudu


async def op():
    async with cli.connection as conn:
        status = await conn.status()
        print(status)


async def op_instead():
    conn = await cli.connect()
    status = await conn.status()
    print(status)
    await conn.close()

if __name__ == "__main__":
    logging.basicConfig(
            level=logging.DEBUG,
            format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s")


    # cli = akudu.Client('192.168.0.111', 7051)
    cli = akudu.Client('192.168.50.112', 7051)
    asyncio.run(op_instead())
    asyncio.run(op())
