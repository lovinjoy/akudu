# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kudu/util/proto_container_test.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='kudu/util/proto_container_test.proto',
  package='kudu',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$kudu/util/proto_container_test.proto\x12\x04kudu\"A\n\x14ProtoContainerTestPB\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\x05\x12\x0c\n\x04note\x18\x03 \x01(\t'
)




_PROTOCONTAINERTESTPB = _descriptor.Descriptor(
  name='ProtoContainerTestPB',
  full_name='kudu.ProtoContainerTestPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='kudu.ProtoContainerTestPB.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='kudu.ProtoContainerTestPB.value', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='note', full_name='kudu.ProtoContainerTestPB.note', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=46,
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['ProtoContainerTestPB'] = _PROTOCONTAINERTESTPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProtoContainerTestPB = _reflection.GeneratedProtocolMessageType('ProtoContainerTestPB', (_message.Message,), {
  'DESCRIPTOR' : _PROTOCONTAINERTESTPB,
  '__module__' : 'kudu.util.proto_container_test_pb2'
  # @@protoc_insertion_point(class_scope:kudu.ProtoContainerTestPB)
  })
_sym_db.RegisterMessage(ProtoContainerTestPB)


# @@protoc_insertion_point(module_scope)
