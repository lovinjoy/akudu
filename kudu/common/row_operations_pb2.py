# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kudu/common/row_operations.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kudu.util import pb_util_pb2 as kudu_dot_util_dot_pb__util__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kudu/common/row_operations.proto',
  package='kudu',
  syntax='proto2',
  serialized_options=b'\n\017org.apache.kudu',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n kudu/common/row_operations.proto\x12\x04kudu\x1a\x17kudu/util/pb_util.proto\"\xd3\x02\n\x0fRowOperationsPB\x12\x12\n\x04rows\x18\x02 \x01(\x0c\x42\x04\x88\xb5\x18\x01\x12\x1b\n\rindirect_data\x18\x03 \x01(\x0c\x42\x04\x88\xb5\x18\x01\"\x8e\x02\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06INSERT\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\x12\n\n\x06UPSERT\x10\x05\x12\x11\n\rINSERT_IGNORE\x10\n\x12\x11\n\rUPDATE_IGNORE\x10\x0b\x12\x11\n\rDELETE_IGNORE\x10\x0c\x12\x11\n\rUPSERT_IGNORE\x10\r\x12\r\n\tSPLIT_ROW\x10\x04\x12\x15\n\x11RANGE_LOWER_BOUND\x10\x06\x12\x15\n\x11RANGE_UPPER_BOUND\x10\x07\x12\x1f\n\x1b\x45XCLUSIVE_RANGE_LOWER_BOUND\x10\x08\x12\x1f\n\x1bINCLUSIVE_RANGE_UPPER_BOUND\x10\tB\x11\n\x0forg.apache.kudu'
  ,
  dependencies=[kudu_dot_util_dot_pb__util__pb2.DESCRIPTOR,])



_ROWOPERATIONSPB_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='kudu.RowOperationsPB.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INSERT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPSERT', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INSERT_IGNORE', index=5, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_IGNORE', index=6, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETE_IGNORE', index=7, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPSERT_IGNORE', index=8, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPLIT_ROW', index=9, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RANGE_LOWER_BOUND', index=10, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RANGE_UPPER_BOUND', index=11, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXCLUSIVE_RANGE_LOWER_BOUND', index=12, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INCLUSIVE_RANGE_UPPER_BOUND', index=13, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=137,
  serialized_end=407,
)
_sym_db.RegisterEnumDescriptor(_ROWOPERATIONSPB_TYPE)


_ROWOPERATIONSPB = _descriptor.Descriptor(
  name='RowOperationsPB',
  full_name='kudu.RowOperationsPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='kudu.RowOperationsPB.rows', index=0,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\210\265\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='indirect_data', full_name='kudu.RowOperationsPB.indirect_data', index=1,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\210\265\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ROWOPERATIONSPB_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=407,
)

_ROWOPERATIONSPB_TYPE.containing_type = _ROWOPERATIONSPB
DESCRIPTOR.message_types_by_name['RowOperationsPB'] = _ROWOPERATIONSPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RowOperationsPB = _reflection.GeneratedProtocolMessageType('RowOperationsPB', (_message.Message,), {
  'DESCRIPTOR' : _ROWOPERATIONSPB,
  '__module__' : 'kudu.common.row_operations_pb2'
  # @@protoc_insertion_point(class_scope:kudu.RowOperationsPB)
  })
_sym_db.RegisterMessage(RowOperationsPB)


DESCRIPTOR._options = None
_ROWOPERATIONSPB.fields_by_name['rows']._options = None
_ROWOPERATIONSPB.fields_by_name['indirect_data']._options = None
# @@protoc_insertion_point(module_scope)
