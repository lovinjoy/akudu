# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kudu/util/hash.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='kudu/util/hash.proto',
  package='kudu',
  syntax='proto2',
  serialized_options=b'\n\017org.apache.kudu',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14kudu/util/hash.proto\x12\x04kudu*R\n\rHashAlgorithm\x12\x10\n\x0cUNKNOWN_HASH\x10\x00\x12\x11\n\rMURMUR_HASH_2\x10\x01\x12\r\n\tCITY_HASH\x10\x02\x12\r\n\tFAST_HASH\x10\x03\x42\x11\n\x0forg.apache.kudu'
)

_HASHALGORITHM = _descriptor.EnumDescriptor(
  name='HashAlgorithm',
  full_name='kudu.HashAlgorithm',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_HASH', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MURMUR_HASH_2', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CITY_HASH', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAST_HASH', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=30,
  serialized_end=112,
)
_sym_db.RegisterEnumDescriptor(_HASHALGORITHM)

HashAlgorithm = enum_type_wrapper.EnumTypeWrapper(_HASHALGORITHM)
UNKNOWN_HASH = 0
MURMUR_HASH_2 = 1
CITY_HASH = 2
FAST_HASH = 3


DESCRIPTOR.enum_types_by_name['HashAlgorithm'] = _HASHALGORITHM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)