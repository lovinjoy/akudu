# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kudu/consensus/log.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kudu.common import common_pb2 as kudu_dot_common_dot_common__pb2
from kudu.consensus import consensus_pb2 as kudu_dot_consensus_dot_consensus__pb2
from kudu.consensus import metadata_pb2 as kudu_dot_consensus_dot_metadata__pb2
from kudu.util.compression import compression_pb2 as kudu_dot_util_dot_compression_dot_compression__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kudu/consensus/log.proto',
  package='kudu.log',
  syntax='proto2',
  serialized_options=b'\n\023org.apache.kudu.log',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18kudu/consensus/log.proto\x12\x08kudu.log\x1a\x18kudu/common/common.proto\x1a\x1ekudu/consensus/consensus.proto\x1a\x1dkudu/consensus/metadata.proto\x1a\'kudu/util/compression/compression.proto\"\x90\x01\n\nLogEntryPB\x12&\n\x04type\x18\x01 \x02(\x0e\x32\x18.kudu.log.LogEntryTypePB\x12/\n\treplicate\x18\x02 \x01(\x0b\x32\x1c.kudu.consensus.ReplicateMsg\x12)\n\x06\x63ommit\x18\x03 \x01(\x0b\x32\x19.kudu.consensus.CommitMsg\"6\n\x0fLogEntryBatchPB\x12#\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x14.kudu.log.LogEntryPB\"\xba\x02\n\x12LogSegmentHeaderPB\x12 \n\x18\x44\x45PRECATED_major_version\x18\x01 \x01(\r\x12 \n\x18\x44\x45PRECATED_minor_version\x18\x02 \x01(\r\x12\x1d\n\x15incompatible_features\x18\n \x03(\x05\x12\x11\n\ttablet_id\x18\x05 \x02(\x0c\x12\x17\n\x0fsequence_number\x18\x06 \x02(\x04\x12\x1e\n\x06schema\x18\x07 \x02(\x0b\x32\x0e.kudu.SchemaPB\x12\x16\n\x0eschema_version\x18\x08 \x01(\r\x12@\n\x11\x63ompression_codec\x18\t \x01(\x0e\x32\x15.kudu.CompressionType:\x0eNO_COMPRESSION\"\x1b\n\x0b\x46\x65\x61tureFlag\x12\x0c\n\x07UNKNOWN\x10\xe7\x07\"\x8b\x01\n\x12LogSegmentFooterPB\x12\x13\n\x0bnum_entries\x18\x01 \x02(\x03\x12\x1f\n\x13min_replicate_index\x18\x02 \x01(\x03:\x02-1\x12\x1f\n\x13max_replicate_index\x18\x03 \x01(\x03:\x02-1\x12\x1e\n\x16\x63lose_timestamp_micros\x18\x04 \x01(\x03*K\n\x0eLogEntryTypePB\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tREPLICATE\x10\x01\x12\n\n\x06\x43OMMIT\x10\x02\x12\x11\n\x0c\x46LUSH_MARKER\x10\xe7\x07\x42\x15\n\x13org.apache.kudu.log'
  ,
  dependencies=[kudu_dot_common_dot_common__pb2.DESCRIPTOR,kudu_dot_consensus_dot_consensus__pb2.DESCRIPTOR,kudu_dot_consensus_dot_metadata__pb2.DESCRIPTOR,kudu_dot_util_dot_compression_dot_compression__pb2.DESCRIPTOR,])

_LOGENTRYTYPEPB = _descriptor.EnumDescriptor(
  name='LogEntryTypePB',
  full_name='kudu.log.LogEntryTypePB',
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
      name='REPLICATE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMMIT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLUSH_MARKER', index=3, number=999,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=830,
  serialized_end=905,
)
_sym_db.RegisterEnumDescriptor(_LOGENTRYTYPEPB)

LogEntryTypePB = enum_type_wrapper.EnumTypeWrapper(_LOGENTRYTYPEPB)
UNKNOWN = 0
REPLICATE = 1
COMMIT = 2
FLUSH_MARKER = 999


_LOGSEGMENTHEADERPB_FEATUREFLAG = _descriptor.EnumDescriptor(
  name='FeatureFlag',
  full_name='kudu.log.LogSegmentHeaderPB.FeatureFlag',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=999,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=659,
  serialized_end=686,
)
_sym_db.RegisterEnumDescriptor(_LOGSEGMENTHEADERPB_FEATUREFLAG)


_LOGENTRYPB = _descriptor.Descriptor(
  name='LogEntryPB',
  full_name='kudu.log.LogEntryPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='kudu.log.LogEntryPB.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='replicate', full_name='kudu.log.LogEntryPB.replicate', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commit', full_name='kudu.log.LogEntryPB.commit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=169,
  serialized_end=313,
)


_LOGENTRYBATCHPB = _descriptor.Descriptor(
  name='LogEntryBatchPB',
  full_name='kudu.log.LogEntryBatchPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='kudu.log.LogEntryBatchPB.entry', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=315,
  serialized_end=369,
)


_LOGSEGMENTHEADERPB = _descriptor.Descriptor(
  name='LogSegmentHeaderPB',
  full_name='kudu.log.LogSegmentHeaderPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DEPRECATED_major_version', full_name='kudu.log.LogSegmentHeaderPB.DEPRECATED_major_version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='DEPRECATED_minor_version', full_name='kudu.log.LogSegmentHeaderPB.DEPRECATED_minor_version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='incompatible_features', full_name='kudu.log.LogSegmentHeaderPB.incompatible_features', index=2,
      number=10, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tablet_id', full_name='kudu.log.LogSegmentHeaderPB.tablet_id', index=3,
      number=5, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='kudu.log.LogSegmentHeaderPB.sequence_number', index=4,
      number=6, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schema', full_name='kudu.log.LogSegmentHeaderPB.schema', index=5,
      number=7, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schema_version', full_name='kudu.log.LogSegmentHeaderPB.schema_version', index=6,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compression_codec', full_name='kudu.log.LogSegmentHeaderPB.compression_codec', index=7,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LOGSEGMENTHEADERPB_FEATUREFLAG,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=686,
)


_LOGSEGMENTFOOTERPB = _descriptor.Descriptor(
  name='LogSegmentFooterPB',
  full_name='kudu.log.LogSegmentFooterPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_entries', full_name='kudu.log.LogSegmentFooterPB.num_entries', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_replicate_index', full_name='kudu.log.LogSegmentFooterPB.min_replicate_index', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_replicate_index', full_name='kudu.log.LogSegmentFooterPB.max_replicate_index', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='close_timestamp_micros', full_name='kudu.log.LogSegmentFooterPB.close_timestamp_micros', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=689,
  serialized_end=828,
)

_LOGENTRYPB.fields_by_name['type'].enum_type = _LOGENTRYTYPEPB
_LOGENTRYPB.fields_by_name['replicate'].message_type = kudu_dot_consensus_dot_consensus__pb2._REPLICATEMSG
_LOGENTRYPB.fields_by_name['commit'].message_type = kudu_dot_consensus_dot_consensus__pb2._COMMITMSG
_LOGENTRYBATCHPB.fields_by_name['entry'].message_type = _LOGENTRYPB
_LOGSEGMENTHEADERPB.fields_by_name['schema'].message_type = kudu_dot_common_dot_common__pb2._SCHEMAPB
_LOGSEGMENTHEADERPB.fields_by_name['compression_codec'].enum_type = kudu_dot_util_dot_compression_dot_compression__pb2._COMPRESSIONTYPE
_LOGSEGMENTHEADERPB_FEATUREFLAG.containing_type = _LOGSEGMENTHEADERPB
DESCRIPTOR.message_types_by_name['LogEntryPB'] = _LOGENTRYPB
DESCRIPTOR.message_types_by_name['LogEntryBatchPB'] = _LOGENTRYBATCHPB
DESCRIPTOR.message_types_by_name['LogSegmentHeaderPB'] = _LOGSEGMENTHEADERPB
DESCRIPTOR.message_types_by_name['LogSegmentFooterPB'] = _LOGSEGMENTFOOTERPB
DESCRIPTOR.enum_types_by_name['LogEntryTypePB'] = _LOGENTRYTYPEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogEntryPB = _reflection.GeneratedProtocolMessageType('LogEntryPB', (_message.Message,), {
  'DESCRIPTOR' : _LOGENTRYPB,
  '__module__' : 'kudu.consensus.log_pb2'
  # @@protoc_insertion_point(class_scope:kudu.log.LogEntryPB)
  })
_sym_db.RegisterMessage(LogEntryPB)

LogEntryBatchPB = _reflection.GeneratedProtocolMessageType('LogEntryBatchPB', (_message.Message,), {
  'DESCRIPTOR' : _LOGENTRYBATCHPB,
  '__module__' : 'kudu.consensus.log_pb2'
  # @@protoc_insertion_point(class_scope:kudu.log.LogEntryBatchPB)
  })
_sym_db.RegisterMessage(LogEntryBatchPB)

LogSegmentHeaderPB = _reflection.GeneratedProtocolMessageType('LogSegmentHeaderPB', (_message.Message,), {
  'DESCRIPTOR' : _LOGSEGMENTHEADERPB,
  '__module__' : 'kudu.consensus.log_pb2'
  # @@protoc_insertion_point(class_scope:kudu.log.LogSegmentHeaderPB)
  })
_sym_db.RegisterMessage(LogSegmentHeaderPB)

LogSegmentFooterPB = _reflection.GeneratedProtocolMessageType('LogSegmentFooterPB', (_message.Message,), {
  'DESCRIPTOR' : _LOGSEGMENTFOOTERPB,
  '__module__' : 'kudu.consensus.log_pb2'
  # @@protoc_insertion_point(class_scope:kudu.log.LogSegmentFooterPB)
  })
_sym_db.RegisterMessage(LogSegmentFooterPB)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)