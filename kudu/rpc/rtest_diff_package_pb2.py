# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kudu/rpc/rtest_diff_package.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='kudu/rpc/rtest_diff_package.proto',
  package='kudu.rpc_test_diff_package',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!kudu/rpc/rtest_diff_package.proto\x12\x1akudu.rpc_test_diff_package\"\x12\n\x10ReqDiffPackagePB\"\x13\n\x11RespDiffPackagePB'
)




_REQDIFFPACKAGEPB = _descriptor.Descriptor(
  name='ReqDiffPackagePB',
  full_name='kudu.rpc_test_diff_package.ReqDiffPackagePB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=83,
)


_RESPDIFFPACKAGEPB = _descriptor.Descriptor(
  name='RespDiffPackagePB',
  full_name='kudu.rpc_test_diff_package.RespDiffPackagePB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=104,
)

DESCRIPTOR.message_types_by_name['ReqDiffPackagePB'] = _REQDIFFPACKAGEPB
DESCRIPTOR.message_types_by_name['RespDiffPackagePB'] = _RESPDIFFPACKAGEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReqDiffPackagePB = _reflection.GeneratedProtocolMessageType('ReqDiffPackagePB', (_message.Message,), {
  'DESCRIPTOR' : _REQDIFFPACKAGEPB,
  '__module__' : 'kudu.rpc.rtest_diff_package_pb2'
  # @@protoc_insertion_point(class_scope:kudu.rpc_test_diff_package.ReqDiffPackagePB)
  })
_sym_db.RegisterMessage(ReqDiffPackagePB)

RespDiffPackagePB = _reflection.GeneratedProtocolMessageType('RespDiffPackagePB', (_message.Message,), {
  'DESCRIPTOR' : _RESPDIFFPACKAGEPB,
  '__module__' : 'kudu.rpc.rtest_diff_package_pb2'
  # @@protoc_insertion_point(class_scope:kudu.rpc_test_diff_package.RespDiffPackagePB)
  })
_sym_db.RegisterMessage(RespDiffPackagePB)


# @@protoc_insertion_point(module_scope)