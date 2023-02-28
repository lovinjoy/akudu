# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kudu/consensus/metadata.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kudu.common import common_pb2 as kudu_dot_common_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kudu/consensus/metadata.proto',
  package='kudu.consensus',
  syntax='proto2',
  serialized_options=b'\n\031org.apache.kudu.consensus',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dkudu/consensus/metadata.proto\x12\x0ekudu.consensus\x1a\x18kudu/common/common.proto\"A\n\x0fRaftPeerAttrsPB\x12\x16\n\x07promote\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x16\n\x07replace\x18\x02 \x01(\x08:\x05\x66\x61lse\"\xa6\x01\n\x0eHealthReportPB\x12\x43\n\x0eoverall_health\x18\x01 \x01(\x0e\x32+.kudu.consensus.HealthReportPB.HealthStatus\"O\n\x0cHealthStatus\x12\x0c\n\x07UNKNOWN\x10\xe7\x07\x12\n\n\x06\x46\x41ILED\x10\x00\x12\x0b\n\x07HEALTHY\x10\x01\x12\x18\n\x14\x46\x41ILED_UNRECOVERABLE\x10\x02\"\x8b\x03\n\nRaftPeerPB\x12\x16\n\x0epermanent_uuid\x18\x01 \x01(\x0c\x12:\n\x0bmember_type\x18\x02 \x01(\x0e\x32%.kudu.consensus.RaftPeerPB.MemberType\x12)\n\x0flast_known_addr\x18\x03 \x01(\x0b\x32\x10.kudu.HostPortPB\x12.\n\x05\x61ttrs\x18\x04 \x01(\x0b\x32\x1f.kudu.consensus.RaftPeerAttrsPB\x12\x35\n\rhealth_report\x18\x05 \x01(\x0b\x32\x1e.kudu.consensus.HealthReportPB\"U\n\x04Role\x12\x11\n\x0cUNKNOWN_ROLE\x10\xe7\x07\x12\x0c\n\x08\x46OLLOWER\x10\x00\x12\n\n\x06LEADER\x10\x01\x12\x0b\n\x07LEARNER\x10\x02\x12\x13\n\x0fNON_PARTICIPANT\x10\x03\"@\n\nMemberType\x12\x18\n\x13UNKNOWN_MEMBER_TYPE\x10\xe7\x07\x12\r\n\tNON_VOTER\x10\x00\x12\t\n\x05VOTER\x10\x01\"\x8a\x01\n\x0cRaftConfigPB\x12\x12\n\nopid_index\x18\x01 \x01(\x03\x12\x16\n\x0eOBSOLETE_local\x18\x02 \x01(\x08\x12#\n\x14unsafe_config_change\x18\x04 \x01(\x08:\x05\x66\x61lse\x12)\n\x05peers\x18\x03 \x03(\x0b\x32\x1a.kudu.consensus.RaftPeerPB\"\xab\x01\n\x10\x43onsensusStatePB\x12\x14\n\x0c\x63urrent_term\x18\x01 \x02(\x03\x12\x13\n\x0bleader_uuid\x18\x02 \x01(\t\x12\x36\n\x10\x63ommitted_config\x18\x03 \x02(\x0b\x32\x1c.kudu.consensus.RaftConfigPB\x12\x34\n\x0epending_config\x18\x04 \x01(\x0b\x32\x1c.kudu.consensus.RaftConfigPB\"v\n\x13\x43onsensusMetadataPB\x12\x36\n\x10\x63ommitted_config\x18\x01 \x02(\x0b\x32\x1c.kudu.consensus.RaftConfigPB\x12\x14\n\x0c\x63urrent_term\x18\x02 \x02(\x03\x12\x11\n\tvoted_for\x18\x03 \x01(\tB\x1b\n\x19org.apache.kudu.consensus'
  ,
  dependencies=[kudu_dot_common_dot_common__pb2.DESCRIPTOR,])



_HEALTHREPORTPB_HEALTHSTATUS = _descriptor.EnumDescriptor(
  name='HealthStatus',
  full_name='kudu.consensus.HealthReportPB.HealthStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=999,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=1, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HEALTHY', index=2, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED_UNRECOVERABLE', index=3, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=230,
  serialized_end=309,
)
_sym_db.RegisterEnumDescriptor(_HEALTHREPORTPB_HEALTHSTATUS)

_RAFTPEERPB_ROLE = _descriptor.EnumDescriptor(
  name='Role',
  full_name='kudu.consensus.RaftPeerPB.Role',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_ROLE', index=0, number=999,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FOLLOWER', index=1, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LEADER', index=2, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LEARNER', index=3, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NON_PARTICIPANT', index=4, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=556,
  serialized_end=641,
)
_sym_db.RegisterEnumDescriptor(_RAFTPEERPB_ROLE)

_RAFTPEERPB_MEMBERTYPE = _descriptor.EnumDescriptor(
  name='MemberType',
  full_name='kudu.consensus.RaftPeerPB.MemberType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_MEMBER_TYPE', index=0, number=999,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NON_VOTER', index=1, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VOTER', index=2, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=643,
  serialized_end=707,
)
_sym_db.RegisterEnumDescriptor(_RAFTPEERPB_MEMBERTYPE)


_RAFTPEERATTRSPB = _descriptor.Descriptor(
  name='RaftPeerAttrsPB',
  full_name='kudu.consensus.RaftPeerAttrsPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='promote', full_name='kudu.consensus.RaftPeerAttrsPB.promote', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='replace', full_name='kudu.consensus.RaftPeerAttrsPB.replace', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=75,
  serialized_end=140,
)


_HEALTHREPORTPB = _descriptor.Descriptor(
  name='HealthReportPB',
  full_name='kudu.consensus.HealthReportPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='overall_health', full_name='kudu.consensus.HealthReportPB.overall_health', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=999,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HEALTHREPORTPB_HEALTHSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=309,
)


_RAFTPEERPB = _descriptor.Descriptor(
  name='RaftPeerPB',
  full_name='kudu.consensus.RaftPeerPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='permanent_uuid', full_name='kudu.consensus.RaftPeerPB.permanent_uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='member_type', full_name='kudu.consensus.RaftPeerPB.member_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=999,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_known_addr', full_name='kudu.consensus.RaftPeerPB.last_known_addr', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attrs', full_name='kudu.consensus.RaftPeerPB.attrs', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='health_report', full_name='kudu.consensus.RaftPeerPB.health_report', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RAFTPEERPB_ROLE,
    _RAFTPEERPB_MEMBERTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=312,
  serialized_end=707,
)


_RAFTCONFIGPB = _descriptor.Descriptor(
  name='RaftConfigPB',
  full_name='kudu.consensus.RaftConfigPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='opid_index', full_name='kudu.consensus.RaftConfigPB.opid_index', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='OBSOLETE_local', full_name='kudu.consensus.RaftConfigPB.OBSOLETE_local', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unsafe_config_change', full_name='kudu.consensus.RaftConfigPB.unsafe_config_change', index=2,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='peers', full_name='kudu.consensus.RaftConfigPB.peers', index=3,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=710,
  serialized_end=848,
)


_CONSENSUSSTATEPB = _descriptor.Descriptor(
  name='ConsensusStatePB',
  full_name='kudu.consensus.ConsensusStatePB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_term', full_name='kudu.consensus.ConsensusStatePB.current_term', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='leader_uuid', full_name='kudu.consensus.ConsensusStatePB.leader_uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='committed_config', full_name='kudu.consensus.ConsensusStatePB.committed_config', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pending_config', full_name='kudu.consensus.ConsensusStatePB.pending_config', index=3,
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
  serialized_start=851,
  serialized_end=1022,
)


_CONSENSUSMETADATAPB = _descriptor.Descriptor(
  name='ConsensusMetadataPB',
  full_name='kudu.consensus.ConsensusMetadataPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='committed_config', full_name='kudu.consensus.ConsensusMetadataPB.committed_config', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='current_term', full_name='kudu.consensus.ConsensusMetadataPB.current_term', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='voted_for', full_name='kudu.consensus.ConsensusMetadataPB.voted_for', index=2,
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
  serialized_start=1024,
  serialized_end=1142,
)

_HEALTHREPORTPB.fields_by_name['overall_health'].enum_type = _HEALTHREPORTPB_HEALTHSTATUS
_HEALTHREPORTPB_HEALTHSTATUS.containing_type = _HEALTHREPORTPB
_RAFTPEERPB.fields_by_name['member_type'].enum_type = _RAFTPEERPB_MEMBERTYPE
_RAFTPEERPB.fields_by_name['last_known_addr'].message_type = kudu_dot_common_dot_common__pb2._HOSTPORTPB
_RAFTPEERPB.fields_by_name['attrs'].message_type = _RAFTPEERATTRSPB
_RAFTPEERPB.fields_by_name['health_report'].message_type = _HEALTHREPORTPB
_RAFTPEERPB_ROLE.containing_type = _RAFTPEERPB
_RAFTPEERPB_MEMBERTYPE.containing_type = _RAFTPEERPB
_RAFTCONFIGPB.fields_by_name['peers'].message_type = _RAFTPEERPB
_CONSENSUSSTATEPB.fields_by_name['committed_config'].message_type = _RAFTCONFIGPB
_CONSENSUSSTATEPB.fields_by_name['pending_config'].message_type = _RAFTCONFIGPB
_CONSENSUSMETADATAPB.fields_by_name['committed_config'].message_type = _RAFTCONFIGPB
DESCRIPTOR.message_types_by_name['RaftPeerAttrsPB'] = _RAFTPEERATTRSPB
DESCRIPTOR.message_types_by_name['HealthReportPB'] = _HEALTHREPORTPB
DESCRIPTOR.message_types_by_name['RaftPeerPB'] = _RAFTPEERPB
DESCRIPTOR.message_types_by_name['RaftConfigPB'] = _RAFTCONFIGPB
DESCRIPTOR.message_types_by_name['ConsensusStatePB'] = _CONSENSUSSTATEPB
DESCRIPTOR.message_types_by_name['ConsensusMetadataPB'] = _CONSENSUSMETADATAPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RaftPeerAttrsPB = _reflection.GeneratedProtocolMessageType('RaftPeerAttrsPB', (_message.Message,), {
  'DESCRIPTOR' : _RAFTPEERATTRSPB,
  '__module__' : 'kudu.consensus.metadata_pb2'
  # @@protoc_insertion_point(class_scope:kudu.consensus.RaftPeerAttrsPB)
  })
_sym_db.RegisterMessage(RaftPeerAttrsPB)

HealthReportPB = _reflection.GeneratedProtocolMessageType('HealthReportPB', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHREPORTPB,
  '__module__' : 'kudu.consensus.metadata_pb2'
  # @@protoc_insertion_point(class_scope:kudu.consensus.HealthReportPB)
  })
_sym_db.RegisterMessage(HealthReportPB)

RaftPeerPB = _reflection.GeneratedProtocolMessageType('RaftPeerPB', (_message.Message,), {
  'DESCRIPTOR' : _RAFTPEERPB,
  '__module__' : 'kudu.consensus.metadata_pb2'
  # @@protoc_insertion_point(class_scope:kudu.consensus.RaftPeerPB)
  })
_sym_db.RegisterMessage(RaftPeerPB)

RaftConfigPB = _reflection.GeneratedProtocolMessageType('RaftConfigPB', (_message.Message,), {
  'DESCRIPTOR' : _RAFTCONFIGPB,
  '__module__' : 'kudu.consensus.metadata_pb2'
  # @@protoc_insertion_point(class_scope:kudu.consensus.RaftConfigPB)
  })
_sym_db.RegisterMessage(RaftConfigPB)

ConsensusStatePB = _reflection.GeneratedProtocolMessageType('ConsensusStatePB', (_message.Message,), {
  'DESCRIPTOR' : _CONSENSUSSTATEPB,
  '__module__' : 'kudu.consensus.metadata_pb2'
  # @@protoc_insertion_point(class_scope:kudu.consensus.ConsensusStatePB)
  })
_sym_db.RegisterMessage(ConsensusStatePB)

ConsensusMetadataPB = _reflection.GeneratedProtocolMessageType('ConsensusMetadataPB', (_message.Message,), {
  'DESCRIPTOR' : _CONSENSUSMETADATAPB,
  '__module__' : 'kudu.consensus.metadata_pb2'
  # @@protoc_insertion_point(class_scope:kudu.consensus.ConsensusMetadataPB)
  })
_sym_db.RegisterMessage(ConsensusMetadataPB)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)