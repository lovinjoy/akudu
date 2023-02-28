# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kudu/server/server_base.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kudu.common import common_pb2 as kudu_dot_common_dot_common__pb2
from kudu.common import wire_protocol_pb2 as kudu_dot_common_dot_wire__protocol__pb2
from kudu.rpc import rpc_header_pb2 as kudu_dot_rpc_dot_rpc__header__pb2
from kudu.util import mem_tracker_pb2 as kudu_dot_util_dot_mem__tracker__pb2
from kudu.util import version_info_pb2 as kudu_dot_util_dot_version__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kudu/server/server_base.proto',
  package='kudu.server',
  syntax='proto2',
  serialized_options=b'\n\026org.apache.kudu.server',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dkudu/server/server_base.proto\x12\x0bkudu.server\x1a\x18kudu/common/common.proto\x1a\x1fkudu/common/wire_protocol.proto\x1a\x19kudu/rpc/rpc_header.proto\x1a\x1bkudu/util/mem_tracker.proto\x1a\x1ckudu/util/version_info.proto\"\xc7\x01\n\x0eServerStatusPB\x12+\n\rnode_instance\x18\x01 \x02(\x0b\x32\x14.kudu.NodeInstancePB\x12-\n\x13\x62ound_rpc_addresses\x18\x02 \x03(\x0b\x32\x10.kudu.HostPortPB\x12.\n\x14\x62ound_http_addresses\x18\x03 \x03(\x0b\x32\x10.kudu.HostPortPB\x12)\n\x0cversion_info\x18\x04 \x01(\x0b\x32\x13.kudu.VersionInfoPB\"C\n\x11GetFlagsRequestPB\x12\x11\n\tall_flags\x18\x01 \x01(\x08\x12\x0c\n\x04tags\x18\x02 \x03(\t\x12\r\n\x05\x66lags\x18\x03 \x03(\t\"\x96\x01\n\x12GetFlagsResponsePB\x12\x33\n\x05\x66lags\x18\x01 \x03(\x0b\x32$.kudu.server.GetFlagsResponsePB.Flag\x1aK\n\x04\x46lag\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0c\n\x04tags\x18\x03 \x03(\t\x12\x18\n\x10is_default_value\x18\x04 \x01(\x08\"k\n\x10SetFlagRequestPB\x12\x0c\n\x04\x66lag\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\x12\x14\n\x05\x66orce\x18\x03 \x01(\x08:\x05\x66\x61lse\x12$\n\x15run_consistency_check\x18\x04 \x01(\x08:\x05\x66\x61lse\"\xb9\x01\n\x11SetFlagResponsePB\x12\x33\n\x06result\x18\x01 \x02(\x0e\x32#.kudu.server.SetFlagResponsePB.Code\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x11\n\told_value\x18\x03 \x01(\t\"O\n\x04\x43ode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x10\n\x0cNO_SUCH_FLAG\x10\x02\x12\r\n\tBAD_VALUE\x10\x03\x12\x0c\n\x08NOT_SAFE\x10\x04\"\x18\n\x16\x46lushCoverageRequestPB\"*\n\x17\x46lushCoverageResponsePB\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x15\n\x13\x43heckLeaksRequestPB\"<\n\x14\x43heckLeaksResponsePB\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x13\n\x0b\x66ound_leaks\x18\x02 \x01(\x08\"\x16\n\x14ServerClockRequestPB\"*\n\x15ServerClockResponsePB\x12\x11\n\ttimestamp\x18\x01 \x01(\x06\"\x14\n\x12GetStatusRequestPB\"d\n\x13GetStatusResponsePB\x12+\n\x06status\x18\x01 \x02(\x0b\x32\x1b.kudu.server.ServerStatusPB\x12 \n\x05\x65rror\x18\x02 \x01(\x0b\x32\x11.kudu.AppStatusPB\"O\n#SetServerWallClockForTestsRequestPB\x12\x10\n\x08now_usec\x18\x01 \x01(\x04\x12\x16\n\x0emax_error_usec\x18\x02 \x01(\x04\"7\n$SetServerWallClockForTestsResponsePB\x12\x0f\n\x07success\x18\x01 \x02(\x08\"\x1a\n\x18\x44umpMemTrackersRequestPB\"E\n\x19\x44umpMemTrackersResponsePB\x12(\n\x0croot_tracker\x18\x01 \x01(\x0b\x32\x12.kudu.MemTrackerPB2\xa4\x06\n\x0eGenericService\x12K\n\x08GetFlags\x12\x1e.kudu.server.GetFlagsRequestPB\x1a\x1f.kudu.server.GetFlagsResponsePB\x12H\n\x07SetFlag\x12\x1d.kudu.server.SetFlagRequestPB\x1a\x1e.kudu.server.SetFlagResponsePB\x12Z\n\rFlushCoverage\x12#.kudu.server.FlushCoverageRequestPB\x1a$.kudu.server.FlushCoverageResponsePB\x12Q\n\nCheckLeaks\x12 .kudu.server.CheckLeaksRequestPB\x1a!.kudu.server.CheckLeaksResponsePB\x12i\n\x0bServerClock\x12!.kudu.server.ServerClockRequestPB\x1a\".kudu.server.ServerClockResponsePB\"\x13\xba\xb5\x18\x0f\x41uthorizeClient\x12\x81\x01\n\x1aSetServerWallClockForTests\x12\x30.kudu.server.SetServerWallClockForTestsRequestPB\x1a\x31.kudu.server.SetServerWallClockForTestsResponsePB\x12\x63\n\tGetStatus\x12\x1f.kudu.server.GetStatusRequestPB\x1a .kudu.server.GetStatusResponsePB\"\x13\xba\xb5\x18\x0f\x41uthorizeClient\x12`\n\x0f\x44umpMemTrackers\x12%.kudu.server.DumpMemTrackersRequestPB\x1a&.kudu.server.DumpMemTrackersResponsePB\x1a\x16\xba\xb5\x18\x12\x41uthorizeSuperUserB\x18\n\x16org.apache.kudu.server'
  ,
  dependencies=[kudu_dot_common_dot_common__pb2.DESCRIPTOR,kudu_dot_common_dot_wire__protocol__pb2.DESCRIPTOR,kudu_dot_rpc_dot_rpc__header__pb2.DESCRIPTOR,kudu_dot_util_dot_mem__tracker__pb2.DESCRIPTOR,kudu_dot_util_dot_version__info__pb2.DESCRIPTOR,])



_SETFLAGRESPONSEPB_CODE = _descriptor.EnumDescriptor(
  name='Code',
  full_name='kudu.server.SetFlagResponsePB.Code',
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
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NO_SUCH_FLAG', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BAD_VALUE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_SAFE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=831,
  serialized_end=910,
)
_sym_db.RegisterEnumDescriptor(_SETFLAGRESPONSEPB_CODE)


_SERVERSTATUSPB = _descriptor.Descriptor(
  name='ServerStatusPB',
  full_name='kudu.server.ServerStatusPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_instance', full_name='kudu.server.ServerStatusPB.node_instance', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bound_rpc_addresses', full_name='kudu.server.ServerStatusPB.bound_rpc_addresses', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bound_http_addresses', full_name='kudu.server.ServerStatusPB.bound_http_addresses', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version_info', full_name='kudu.server.ServerStatusPB.version_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=192,
  serialized_end=391,
)


_GETFLAGSREQUESTPB = _descriptor.Descriptor(
  name='GetFlagsRequestPB',
  full_name='kudu.server.GetFlagsRequestPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='all_flags', full_name='kudu.server.GetFlagsRequestPB.all_flags', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='kudu.server.GetFlagsRequestPB.tags', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flags', full_name='kudu.server.GetFlagsRequestPB.flags', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=393,
  serialized_end=460,
)


_GETFLAGSRESPONSEPB_FLAG = _descriptor.Descriptor(
  name='Flag',
  full_name='kudu.server.GetFlagsResponsePB.Flag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='kudu.server.GetFlagsResponsePB.Flag.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='kudu.server.GetFlagsResponsePB.Flag.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='kudu.server.GetFlagsResponsePB.Flag.tags', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_default_value', full_name='kudu.server.GetFlagsResponsePB.Flag.is_default_value', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=538,
  serialized_end=613,
)

_GETFLAGSRESPONSEPB = _descriptor.Descriptor(
  name='GetFlagsResponsePB',
  full_name='kudu.server.GetFlagsResponsePB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flags', full_name='kudu.server.GetFlagsResponsePB.flags', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GETFLAGSRESPONSEPB_FLAG, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=463,
  serialized_end=613,
)


_SETFLAGREQUESTPB = _descriptor.Descriptor(
  name='SetFlagRequestPB',
  full_name='kudu.server.SetFlagRequestPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag', full_name='kudu.server.SetFlagRequestPB.flag', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='kudu.server.SetFlagRequestPB.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='force', full_name='kudu.server.SetFlagRequestPB.force', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='run_consistency_check', full_name='kudu.server.SetFlagRequestPB.run_consistency_check', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=615,
  serialized_end=722,
)


_SETFLAGRESPONSEPB = _descriptor.Descriptor(
  name='SetFlagResponsePB',
  full_name='kudu.server.SetFlagResponsePB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='kudu.server.SetFlagResponsePB.result', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='kudu.server.SetFlagResponsePB.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='old_value', full_name='kudu.server.SetFlagResponsePB.old_value', index=2,
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
    _SETFLAGRESPONSEPB_CODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=725,
  serialized_end=910,
)


_FLUSHCOVERAGEREQUESTPB = _descriptor.Descriptor(
  name='FlushCoverageRequestPB',
  full_name='kudu.server.FlushCoverageRequestPB',
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
  serialized_start=912,
  serialized_end=936,
)


_FLUSHCOVERAGERESPONSEPB = _descriptor.Descriptor(
  name='FlushCoverageResponsePB',
  full_name='kudu.server.FlushCoverageResponsePB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='kudu.server.FlushCoverageResponsePB.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=938,
  serialized_end=980,
)


_CHECKLEAKSREQUESTPB = _descriptor.Descriptor(
  name='CheckLeaksRequestPB',
  full_name='kudu.server.CheckLeaksRequestPB',
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
  serialized_start=982,
  serialized_end=1003,
)


_CHECKLEAKSRESPONSEPB = _descriptor.Descriptor(
  name='CheckLeaksResponsePB',
  full_name='kudu.server.CheckLeaksResponsePB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='kudu.server.CheckLeaksResponsePB.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='found_leaks', full_name='kudu.server.CheckLeaksResponsePB.found_leaks', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1005,
  serialized_end=1065,
)


_SERVERCLOCKREQUESTPB = _descriptor.Descriptor(
  name='ServerClockRequestPB',
  full_name='kudu.server.ServerClockRequestPB',
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
  serialized_start=1067,
  serialized_end=1089,
)


_SERVERCLOCKRESPONSEPB = _descriptor.Descriptor(
  name='ServerClockResponsePB',
  full_name='kudu.server.ServerClockResponsePB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='kudu.server.ServerClockResponsePB.timestamp', index=0,
      number=1, type=6, cpp_type=4, label=1,
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
  serialized_start=1091,
  serialized_end=1133,
)


_GETSTATUSREQUESTPB = _descriptor.Descriptor(
  name='GetStatusRequestPB',
  full_name='kudu.server.GetStatusRequestPB',
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
  serialized_start=1135,
  serialized_end=1155,
)


_GETSTATUSRESPONSEPB = _descriptor.Descriptor(
  name='GetStatusResponsePB',
  full_name='kudu.server.GetStatusResponsePB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='kudu.server.GetStatusResponsePB.status', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='kudu.server.GetStatusResponsePB.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1157,
  serialized_end=1257,
)


_SETSERVERWALLCLOCKFORTESTSREQUESTPB = _descriptor.Descriptor(
  name='SetServerWallClockForTestsRequestPB',
  full_name='kudu.server.SetServerWallClockForTestsRequestPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='now_usec', full_name='kudu.server.SetServerWallClockForTestsRequestPB.now_usec', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_error_usec', full_name='kudu.server.SetServerWallClockForTestsRequestPB.max_error_usec', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=1259,
  serialized_end=1338,
)


_SETSERVERWALLCLOCKFORTESTSRESPONSEPB = _descriptor.Descriptor(
  name='SetServerWallClockForTestsResponsePB',
  full_name='kudu.server.SetServerWallClockForTestsResponsePB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='kudu.server.SetServerWallClockForTestsResponsePB.success', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=1340,
  serialized_end=1395,
)


_DUMPMEMTRACKERSREQUESTPB = _descriptor.Descriptor(
  name='DumpMemTrackersRequestPB',
  full_name='kudu.server.DumpMemTrackersRequestPB',
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
  serialized_start=1397,
  serialized_end=1423,
)


_DUMPMEMTRACKERSRESPONSEPB = _descriptor.Descriptor(
  name='DumpMemTrackersResponsePB',
  full_name='kudu.server.DumpMemTrackersResponsePB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='root_tracker', full_name='kudu.server.DumpMemTrackersResponsePB.root_tracker', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=1425,
  serialized_end=1494,
)

_SERVERSTATUSPB.fields_by_name['node_instance'].message_type = kudu_dot_common_dot_wire__protocol__pb2._NODEINSTANCEPB
_SERVERSTATUSPB.fields_by_name['bound_rpc_addresses'].message_type = kudu_dot_common_dot_common__pb2._HOSTPORTPB
_SERVERSTATUSPB.fields_by_name['bound_http_addresses'].message_type = kudu_dot_common_dot_common__pb2._HOSTPORTPB
_SERVERSTATUSPB.fields_by_name['version_info'].message_type = kudu_dot_util_dot_version__info__pb2._VERSIONINFOPB
_GETFLAGSRESPONSEPB_FLAG.containing_type = _GETFLAGSRESPONSEPB
_GETFLAGSRESPONSEPB.fields_by_name['flags'].message_type = _GETFLAGSRESPONSEPB_FLAG
_SETFLAGRESPONSEPB.fields_by_name['result'].enum_type = _SETFLAGRESPONSEPB_CODE
_SETFLAGRESPONSEPB_CODE.containing_type = _SETFLAGRESPONSEPB
_GETSTATUSRESPONSEPB.fields_by_name['status'].message_type = _SERVERSTATUSPB
_GETSTATUSRESPONSEPB.fields_by_name['error'].message_type = kudu_dot_common_dot_wire__protocol__pb2._APPSTATUSPB
_DUMPMEMTRACKERSRESPONSEPB.fields_by_name['root_tracker'].message_type = kudu_dot_util_dot_mem__tracker__pb2._MEMTRACKERPB
DESCRIPTOR.message_types_by_name['ServerStatusPB'] = _SERVERSTATUSPB
DESCRIPTOR.message_types_by_name['GetFlagsRequestPB'] = _GETFLAGSREQUESTPB
DESCRIPTOR.message_types_by_name['GetFlagsResponsePB'] = _GETFLAGSRESPONSEPB
DESCRIPTOR.message_types_by_name['SetFlagRequestPB'] = _SETFLAGREQUESTPB
DESCRIPTOR.message_types_by_name['SetFlagResponsePB'] = _SETFLAGRESPONSEPB
DESCRIPTOR.message_types_by_name['FlushCoverageRequestPB'] = _FLUSHCOVERAGEREQUESTPB
DESCRIPTOR.message_types_by_name['FlushCoverageResponsePB'] = _FLUSHCOVERAGERESPONSEPB
DESCRIPTOR.message_types_by_name['CheckLeaksRequestPB'] = _CHECKLEAKSREQUESTPB
DESCRIPTOR.message_types_by_name['CheckLeaksResponsePB'] = _CHECKLEAKSRESPONSEPB
DESCRIPTOR.message_types_by_name['ServerClockRequestPB'] = _SERVERCLOCKREQUESTPB
DESCRIPTOR.message_types_by_name['ServerClockResponsePB'] = _SERVERCLOCKRESPONSEPB
DESCRIPTOR.message_types_by_name['GetStatusRequestPB'] = _GETSTATUSREQUESTPB
DESCRIPTOR.message_types_by_name['GetStatusResponsePB'] = _GETSTATUSRESPONSEPB
DESCRIPTOR.message_types_by_name['SetServerWallClockForTestsRequestPB'] = _SETSERVERWALLCLOCKFORTESTSREQUESTPB
DESCRIPTOR.message_types_by_name['SetServerWallClockForTestsResponsePB'] = _SETSERVERWALLCLOCKFORTESTSRESPONSEPB
DESCRIPTOR.message_types_by_name['DumpMemTrackersRequestPB'] = _DUMPMEMTRACKERSREQUESTPB
DESCRIPTOR.message_types_by_name['DumpMemTrackersResponsePB'] = _DUMPMEMTRACKERSRESPONSEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerStatusPB = _reflection.GeneratedProtocolMessageType('ServerStatusPB', (_message.Message,), {
  'DESCRIPTOR' : _SERVERSTATUSPB,
  '__module__' : 'kudu.server.server_base_pb2'
  # @@protoc_insertion_point(class_scope:kudu.server.ServerStatusPB)
  })
_sym_db.RegisterMessage(ServerStatusPB)

GetFlagsRequestPB = _reflection.GeneratedProtocolMessageType('GetFlagsRequestPB', (_message.Message,), {
  'DESCRIPTOR' : _GETFLAGSREQUESTPB,
  '__module__' : 'kudu.server.server_base_pb2'
  # @@protoc_insertion_point(class_scope:kudu.server.GetFlagsRequestPB)
  })
_sym_db.RegisterMessage(GetFlagsRequestPB)

GetFlagsResponsePB = _reflection.GeneratedProtocolMessageType('GetFlagsResponsePB', (_message.Message,), {

  'Flag' : _reflection.GeneratedProtocolMessageType('Flag', (_message.Message,), {
    'DESCRIPTOR' : _GETFLAGSRESPONSEPB_FLAG,
    '__module__' : 'kudu.server.server_base_pb2'
    # @@protoc_insertion_point(class_scope:kudu.server.GetFlagsResponsePB.Flag)
    })
  ,
  'DESCRIPTOR' : _GETFLAGSRESPONSEPB,
  '__module__' : 'kudu.server.server_base_pb2'
  # @@protoc_insertion_point(class_scope:kudu.server.GetFlagsResponsePB)
  })
_sym_db.RegisterMessage(GetFlagsResponsePB)
_sym_db.RegisterMessage(GetFlagsResponsePB.Flag)

SetFlagRequestPB = _reflection.GeneratedProtocolMessageType('SetFlagRequestPB', (_message.Message,), {
  'DESCRIPTOR' : _SETFLAGREQUESTPB,
  '__module__' : 'kudu.server.server_base_pb2'
  # @@protoc_insertion_point(class_scope:kudu.server.SetFlagRequestPB)
  })
_sym_db.RegisterMessage(SetFlagRequestPB)

SetFlagResponsePB = _reflection.GeneratedProtocolMessageType('SetFlagResponsePB', (_message.Message,), {
  'DESCRIPTOR' : _SETFLAGRESPONSEPB,
  '__module__' : 'kudu.server.server_base_pb2'
  # @@protoc_insertion_point(class_scope:kudu.server.SetFlagResponsePB)
  })
_sym_db.RegisterMessage(SetFlagResponsePB)

FlushCoverageRequestPB = _reflection.GeneratedProtocolMessageType('FlushCoverageRequestPB', (_message.Message,), {
  'DESCRIPTOR' : _FLUSHCOVERAGEREQUESTPB,
  '__module__' : 'kudu.server.server_base_pb2'
  # @@protoc_insertion_point(class_scope:kudu.server.FlushCoverageRequestPB)
  })
_sym_db.RegisterMessage(FlushCoverageRequestPB)

FlushCoverageResponsePB = _reflection.GeneratedProtocolMessageType('FlushCoverageResponsePB', (_message.Message,), {
  'DESCRIPTOR' : _FLUSHCOVERAGERESPONSEPB,
  '__module__' : 'kudu.server.server_base_pb2'
  # @@protoc_insertion_point(class_scope:kudu.server.FlushCoverageResponsePB)
  })
_sym_db.RegisterMessage(FlushCoverageResponsePB)

CheckLeaksRequestPB = _reflection.GeneratedProtocolMessageType('CheckLeaksRequestPB', (_message.Message,), {
  'DESCRIPTOR' : _CHECKLEAKSREQUESTPB,
  '__module__' : 'kudu.server.server_base_pb2'
  # @@protoc_insertion_point(class_scope:kudu.server.CheckLeaksRequestPB)
  })
_sym_db.RegisterMessage(CheckLeaksRequestPB)

CheckLeaksResponsePB = _reflection.GeneratedProtocolMessageType('CheckLeaksResponsePB', (_message.Message,), {
  'DESCRIPTOR' : _CHECKLEAKSRESPONSEPB,
  '__module__' : 'kudu.server.server_base_pb2'
  # @@protoc_insertion_point(class_scope:kudu.server.CheckLeaksResponsePB)
  })
_sym_db.RegisterMessage(CheckLeaksResponsePB)

ServerClockRequestPB = _reflection.GeneratedProtocolMessageType('ServerClockRequestPB', (_message.Message,), {
  'DESCRIPTOR' : _SERVERCLOCKREQUESTPB,
  '__module__' : 'kudu.server.server_base_pb2'
  # @@protoc_insertion_point(class_scope:kudu.server.ServerClockRequestPB)
  })
_sym_db.RegisterMessage(ServerClockRequestPB)

ServerClockResponsePB = _reflection.GeneratedProtocolMessageType('ServerClockResponsePB', (_message.Message,), {
  'DESCRIPTOR' : _SERVERCLOCKRESPONSEPB,
  '__module__' : 'kudu.server.server_base_pb2'
  # @@protoc_insertion_point(class_scope:kudu.server.ServerClockResponsePB)
  })
_sym_db.RegisterMessage(ServerClockResponsePB)

GetStatusRequestPB = _reflection.GeneratedProtocolMessageType('GetStatusRequestPB', (_message.Message,), {
  'DESCRIPTOR' : _GETSTATUSREQUESTPB,
  '__module__' : 'kudu.server.server_base_pb2'
  # @@protoc_insertion_point(class_scope:kudu.server.GetStatusRequestPB)
  })
_sym_db.RegisterMessage(GetStatusRequestPB)

GetStatusResponsePB = _reflection.GeneratedProtocolMessageType('GetStatusResponsePB', (_message.Message,), {
  'DESCRIPTOR' : _GETSTATUSRESPONSEPB,
  '__module__' : 'kudu.server.server_base_pb2'
  # @@protoc_insertion_point(class_scope:kudu.server.GetStatusResponsePB)
  })
_sym_db.RegisterMessage(GetStatusResponsePB)

SetServerWallClockForTestsRequestPB = _reflection.GeneratedProtocolMessageType('SetServerWallClockForTestsRequestPB', (_message.Message,), {
  'DESCRIPTOR' : _SETSERVERWALLCLOCKFORTESTSREQUESTPB,
  '__module__' : 'kudu.server.server_base_pb2'
  # @@protoc_insertion_point(class_scope:kudu.server.SetServerWallClockForTestsRequestPB)
  })
_sym_db.RegisterMessage(SetServerWallClockForTestsRequestPB)

SetServerWallClockForTestsResponsePB = _reflection.GeneratedProtocolMessageType('SetServerWallClockForTestsResponsePB', (_message.Message,), {
  'DESCRIPTOR' : _SETSERVERWALLCLOCKFORTESTSRESPONSEPB,
  '__module__' : 'kudu.server.server_base_pb2'
  # @@protoc_insertion_point(class_scope:kudu.server.SetServerWallClockForTestsResponsePB)
  })
_sym_db.RegisterMessage(SetServerWallClockForTestsResponsePB)

DumpMemTrackersRequestPB = _reflection.GeneratedProtocolMessageType('DumpMemTrackersRequestPB', (_message.Message,), {
  'DESCRIPTOR' : _DUMPMEMTRACKERSREQUESTPB,
  '__module__' : 'kudu.server.server_base_pb2'
  # @@protoc_insertion_point(class_scope:kudu.server.DumpMemTrackersRequestPB)
  })
_sym_db.RegisterMessage(DumpMemTrackersRequestPB)

DumpMemTrackersResponsePB = _reflection.GeneratedProtocolMessageType('DumpMemTrackersResponsePB', (_message.Message,), {
  'DESCRIPTOR' : _DUMPMEMTRACKERSRESPONSEPB,
  '__module__' : 'kudu.server.server_base_pb2'
  # @@protoc_insertion_point(class_scope:kudu.server.DumpMemTrackersResponsePB)
  })
_sym_db.RegisterMessage(DumpMemTrackersResponsePB)


DESCRIPTOR._options = None

_GENERICSERVICE = _descriptor.ServiceDescriptor(
  name='GenericService',
  full_name='kudu.server.GenericService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\272\265\030\022AuthorizeSuperUser',
  create_key=_descriptor._internal_create_key,
  serialized_start=1497,
  serialized_end=2301,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFlags',
    full_name='kudu.server.GenericService.GetFlags',
    index=0,
    containing_service=None,
    input_type=_GETFLAGSREQUESTPB,
    output_type=_GETFLAGSRESPONSEPB,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetFlag',
    full_name='kudu.server.GenericService.SetFlag',
    index=1,
    containing_service=None,
    input_type=_SETFLAGREQUESTPB,
    output_type=_SETFLAGRESPONSEPB,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FlushCoverage',
    full_name='kudu.server.GenericService.FlushCoverage',
    index=2,
    containing_service=None,
    input_type=_FLUSHCOVERAGEREQUESTPB,
    output_type=_FLUSHCOVERAGERESPONSEPB,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CheckLeaks',
    full_name='kudu.server.GenericService.CheckLeaks',
    index=3,
    containing_service=None,
    input_type=_CHECKLEAKSREQUESTPB,
    output_type=_CHECKLEAKSRESPONSEPB,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ServerClock',
    full_name='kudu.server.GenericService.ServerClock',
    index=4,
    containing_service=None,
    input_type=_SERVERCLOCKREQUESTPB,
    output_type=_SERVERCLOCKRESPONSEPB,
    serialized_options=b'\272\265\030\017AuthorizeClient',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetServerWallClockForTests',
    full_name='kudu.server.GenericService.SetServerWallClockForTests',
    index=5,
    containing_service=None,
    input_type=_SETSERVERWALLCLOCKFORTESTSREQUESTPB,
    output_type=_SETSERVERWALLCLOCKFORTESTSRESPONSEPB,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetStatus',
    full_name='kudu.server.GenericService.GetStatus',
    index=6,
    containing_service=None,
    input_type=_GETSTATUSREQUESTPB,
    output_type=_GETSTATUSRESPONSEPB,
    serialized_options=b'\272\265\030\017AuthorizeClient',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DumpMemTrackers',
    full_name='kudu.server.GenericService.DumpMemTrackers',
    index=7,
    containing_service=None,
    input_type=_DUMPMEMTRACKERSREQUESTPB,
    output_type=_DUMPMEMTRACKERSRESPONSEPB,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GENERICSERVICE)

DESCRIPTOR.services_by_name['GenericService'] = _GENERICSERVICE

# @@protoc_insertion_point(module_scope)