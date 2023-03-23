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
    await asyncio.sleep(2)
    print( await conn.status())
    await conn.close()


async def list_tables():
    t = await cli.list_tables()
    print(t.body.tables[:2])
    print('............')
    print(t.body.tables[0].name, t.body.tables[0].num_tablets)


if __name__ == "__main__":
    logging.basicConfig(
            level=logging.DEBUG,
            format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s")


    cli = akudu.Client('192.168.50.112', 7051)
    asyncio.run(op())
    # asyncio.run(op_instead())
    asyncio.run(list_tables())
