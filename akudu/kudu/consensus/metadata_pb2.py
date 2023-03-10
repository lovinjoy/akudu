# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: akudu/kudu/consensus/metadata.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from akudu.kudu.common import common_pb2 as akudu_dot_kudu_dot_common_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#akudu/kudu/consensus/metadata.proto\x12\x0ekudu.consensus\x1a\x1e\x61kudu/kudu/common/common.proto\"A\n\x0fRaftPeerAttrsPB\x12\x16\n\x07promote\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x16\n\x07replace\x18\x02 \x01(\x08:\x05\x66\x61lse\"\xa6\x01\n\x0eHealthReportPB\x12\x43\n\x0eoverall_health\x18\x01 \x01(\x0e\x32+.kudu.consensus.HealthReportPB.HealthStatus\"O\n\x0cHealthStatus\x12\x0c\n\x07UNKNOWN\x10\xe7\x07\x12\n\n\x06\x46\x41ILED\x10\x00\x12\x0b\n\x07HEALTHY\x10\x01\x12\x18\n\x14\x46\x41ILED_UNRECOVERABLE\x10\x02\"\x8b\x03\n\nRaftPeerPB\x12\x16\n\x0epermanent_uuid\x18\x01 \x01(\x0c\x12:\n\x0bmember_type\x18\x02 \x01(\x0e\x32%.kudu.consensus.RaftPeerPB.MemberType\x12)\n\x0flast_known_addr\x18\x03 \x01(\x0b\x32\x10.kudu.HostPortPB\x12.\n\x05\x61ttrs\x18\x04 \x01(\x0b\x32\x1f.kudu.consensus.RaftPeerAttrsPB\x12\x35\n\rhealth_report\x18\x05 \x01(\x0b\x32\x1e.kudu.consensus.HealthReportPB\"U\n\x04Role\x12\x11\n\x0cUNKNOWN_ROLE\x10\xe7\x07\x12\x0c\n\x08\x46OLLOWER\x10\x00\x12\n\n\x06LEADER\x10\x01\x12\x0b\n\x07LEARNER\x10\x02\x12\x13\n\x0fNON_PARTICIPANT\x10\x03\"@\n\nMemberType\x12\x18\n\x13UNKNOWN_MEMBER_TYPE\x10\xe7\x07\x12\r\n\tNON_VOTER\x10\x00\x12\t\n\x05VOTER\x10\x01\"\x8a\x01\n\x0cRaftConfigPB\x12\x12\n\nopid_index\x18\x01 \x01(\x03\x12\x16\n\x0eOBSOLETE_local\x18\x02 \x01(\x08\x12#\n\x14unsafe_config_change\x18\x04 \x01(\x08:\x05\x66\x61lse\x12)\n\x05peers\x18\x03 \x03(\x0b\x32\x1a.kudu.consensus.RaftPeerPB\"\xab\x01\n\x10\x43onsensusStatePB\x12\x14\n\x0c\x63urrent_term\x18\x01 \x02(\x03\x12\x13\n\x0bleader_uuid\x18\x02 \x01(\t\x12\x36\n\x10\x63ommitted_config\x18\x03 \x02(\x0b\x32\x1c.kudu.consensus.RaftConfigPB\x12\x34\n\x0epending_config\x18\x04 \x01(\x0b\x32\x1c.kudu.consensus.RaftConfigPB\"v\n\x13\x43onsensusMetadataPB\x12\x36\n\x10\x63ommitted_config\x18\x01 \x02(\x0b\x32\x1c.kudu.consensus.RaftConfigPB\x12\x14\n\x0c\x63urrent_term\x18\x02 \x02(\x03\x12\x11\n\tvoted_for\x18\x03 \x01(\tB\x1b\n\x19org.apache.kudu.consensus')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akudu.kudu.consensus.metadata_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031org.apache.kudu.consensus'
  _RAFTPEERATTRSPB._serialized_start=87
  _RAFTPEERATTRSPB._serialized_end=152
  _HEALTHREPORTPB._serialized_start=155
  _HEALTHREPORTPB._serialized_end=321
  _HEALTHREPORTPB_HEALTHSTATUS._serialized_start=242
  _HEALTHREPORTPB_HEALTHSTATUS._serialized_end=321
  _RAFTPEERPB._serialized_start=324
  _RAFTPEERPB._serialized_end=719
  _RAFTPEERPB_ROLE._serialized_start=568
  _RAFTPEERPB_ROLE._serialized_end=653
  _RAFTPEERPB_MEMBERTYPE._serialized_start=655
  _RAFTPEERPB_MEMBERTYPE._serialized_end=719
  _RAFTCONFIGPB._serialized_start=722
  _RAFTCONFIGPB._serialized_end=860
  _CONSENSUSSTATEPB._serialized_start=863
  _CONSENSUSSTATEPB._serialized_end=1034
  _CONSENSUSMETADATAPB._serialized_start=1036
  _CONSENSUSMETADATAPB._serialized_end=1154
# @@protoc_insertion_point(module_scope)
