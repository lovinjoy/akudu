# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: akudu/kudu/transactions/transactions.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*akudu/kudu/transactions/transactions.proto\x12\x11kudu.transactions\"\xa4\x01\n\x10TxnStatusEntryPB\x12,\n\x05state\x18\x01 \x01(\x0e\x32\x1d.kudu.transactions.TxnStatePB\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x18\n\x10\x63ommit_timestamp\x18\x03 \x01(\x06\x12\x17\n\x0fstart_timestamp\x18\x04 \x01(\x03\x12!\n\x19last_transition_timestamp\x18\x05 \x01(\x03\"E\n\x15TxnParticipantEntryPB\x12,\n\x05state\x18\x01 \x01(\x0e\x32\x1d.kudu.transactions.TxnStatePB\"P\n\nTxnTokenPB\x12\x0e\n\x06txn_id\x18\x01 \x01(\x03\x12\x18\n\x10keepalive_millis\x18\x02 \x01(\r\x12\x18\n\x10\x65nable_keepalive\x18\x03 \x01(\x08*\x88\x01\n\nTxnStatePB\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04OPEN\x10\x01\x12\x15\n\x11\x41\x42ORT_IN_PROGRESS\x10\x05\x12\x0b\n\x07\x41\x42ORTED\x10\x02\x12\x16\n\x12\x43OMMIT_IN_PROGRESS\x10\x03\x12\x18\n\x14\x46INALIZE_IN_PROGRESS\x10\x06\x12\r\n\tCOMMITTED\x10\x04\x42\x1e\n\x1corg.apache.kudu.transactions')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akudu.kudu.transactions.transactions_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034org.apache.kudu.transactions'
  _TXNSTATEPB._serialized_start=386
  _TXNSTATEPB._serialized_end=522
  _TXNSTATUSENTRYPB._serialized_start=66
  _TXNSTATUSENTRYPB._serialized_end=230
  _TXNPARTICIPANTENTRYPB._serialized_start=232
  _TXNPARTICIPANTENTRYPB._serialized_end=301
  _TXNTOKENPB._serialized_start=303
  _TXNTOKENPB._serialized_end=383
# @@protoc_insertion_point(module_scope)
