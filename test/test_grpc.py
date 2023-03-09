#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Test grpc
"""
__author__ = 'Zagfai'
__date__ = '2023-02'

import grpc

import kudu.server.server_base_pb2 as spb
import kudu.server.server_base_pb2_grpc as sbg

import kudu.master.master_pb2 as mb
import kudu.master.master_pb2_grpc as mg

import kudu.rpc.rpc_header_pb2 as hb
import kudu.rpc.rpc_header_pb2_grpc as bg


def run():
    with grpc.insecure_channel('192.168.50.112:7051') as channel:
        #snb = hb.NegotiatePB(step=1)
        #shb = hb.RequestHeader(call_id=-33)
        #channel.
        stub = mg.MasterServiceStub(channel)
        response = stub.ListTables(mb.ListTablesRequestPB())
        print("Greeter client received following from server: " + response.message)
run()

# def run():
#    with grpc.insecure_channel('192.168.50.112:7051') as channel:
#       stub = sbg.GenericServiceStub(channel)
#       response = stub.GetStatus(0)
#    print("Greeter client received following from server: " + response.message)
# run()
