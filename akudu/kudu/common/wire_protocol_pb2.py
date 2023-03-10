# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: akudu/kudu/common/wire_protocol.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from akudu.kudu.common import common_pb2 as akudu_dot_kudu_dot_common_dot_common__pb2
from akudu.kudu.consensus import metadata_pb2 as akudu_dot_kudu_dot_consensus_dot_metadata__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%akudu/kudu/common/wire_protocol.proto\x12\x04kudu\x1a\x1e\x61kudu/kudu/common/common.proto\x1a#akudu/kudu/consensus/metadata.proto\"\xf1\x03\n\x0b\x41ppStatusPB\x12)\n\x04\x63ode\x18\x01 \x02(\x0e\x32\x1b.kudu.AppStatusPB.ErrorCode\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x12\n\nposix_code\x18\x04 \x01(\x05\"\x91\x03\n\tErrorCode\x12\x12\n\rUNKNOWN_ERROR\x10\xe7\x07\x12\x06\n\x02OK\x10\x00\x12\r\n\tNOT_FOUND\x10\x01\x12\x0e\n\nCORRUPTION\x10\x02\x12\x11\n\rNOT_SUPPORTED\x10\x03\x12\x14\n\x10INVALID_ARGUMENT\x10\x04\x12\x0c\n\x08IO_ERROR\x10\x05\x12\x13\n\x0f\x41LREADY_PRESENT\x10\x06\x12\x11\n\rRUNTIME_ERROR\x10\x07\x12\x11\n\rNETWORK_ERROR\x10\x08\x12\x11\n\rILLEGAL_STATE\x10\t\x12\x12\n\x0eNOT_AUTHORIZED\x10\n\x12\x0b\n\x07\x41\x42ORTED\x10\x0b\x12\x10\n\x0cREMOTE_ERROR\x10\x0c\x12\x17\n\x13SERVICE_UNAVAILABLE\x10\r\x12\r\n\tTIMED_OUT\x10\x0e\x12\x11\n\rUNINITIALIZED\x10\x0f\x12\x17\n\x13\x43ONFIGURATION_ERROR\x10\x10\x12\x0e\n\nINCOMPLETE\x10\x11\x12\x0f\n\x0b\x45ND_OF_FILE\x10\x12\x12\r\n\tCANCELLED\x10\x13\x12\r\n\tIMMUTABLE\x10\x14\"@\n\x0eNodeInstancePB\x12\x16\n\x0epermanent_uuid\x18\x01 \x02(\x0c\x12\x16\n\x0einstance_seqno\x18\x02 \x02(\x03\"\xae\x02\n\x14ServerRegistrationPB\x12\'\n\rrpc_addresses\x18\x01 \x03(\x0b\x32\x10.kudu.HostPortPB\x12(\n\x0ehttp_addresses\x18\x02 \x03(\x0b\x32\x10.kudu.HostPortPB\x12-\n\x13rpc_proxy_addresses\x18\x07 \x03(\x0b\x32\x10.kudu.HostPortPB\x12.\n\x14http_proxy_addresses\x18\x08 \x03(\x0b\x32\x10.kudu.HostPortPB\x12\x18\n\x10software_version\x18\x03 \x01(\t\x12\x15\n\rhttps_enabled\x18\x04 \x01(\x08\x12\x12\n\nstart_time\x18\x05 \x01(\x03\x12\x1f\n\x17unix_domain_socket_path\x18\x06 \x01(\t\"\x8d\x02\n\rServerEntryPB\x12 \n\x05\x65rror\x18\x01 \x01(\x0b\x32\x11.kudu.AppStatusPB\x12)\n\x0binstance_id\x18\x02 \x01(\x0b\x32\x14.kudu.NodeInstancePB\x12\x30\n\x0cregistration\x18\x03 \x01(\x0b\x32\x1a.kudu.ServerRegistrationPB\x12-\n\x04role\x18\x04 \x01(\x0e\x32\x1f.kudu.consensus.RaftPeerPB.Role\x12\x12\n\ncluster_id\x18\x05 \x01(\t\x12:\n\x0bmember_type\x18\x06 \x01(\x0e\x32%.kudu.consensus.RaftPeerPB.MemberType\"]\n\x11RowwiseRowBlockPB\x12\x13\n\x08num_rows\x18\x01 \x01(\x05:\x01\x30\x12\x14\n\x0crows_sidecar\x18\x02 \x01(\x05\x12\x1d\n\x15indirect_data_sidecar\x18\x03 \x01(\x05\"\xb6\x01\n\x12\x43olumnarRowBlockPB\x12\x30\n\x07\x63olumns\x18\x01 \x03(\x0b\x32\x1f.kudu.ColumnarRowBlockPB.Column\x12\x10\n\x08num_rows\x18\x02 \x01(\x03\x1a\\\n\x06\x43olumn\x12\x14\n\x0c\x64\x61ta_sidecar\x18\x01 \x01(\x05\x12\x1b\n\x13varlen_data_sidecar\x18\x02 \x01(\x05\x12\x1f\n\x17non_null_bitmap_sidecar\x18\x03 \x01(\x05\x42\x11\n\x0forg.apache.kudu')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akudu.kudu.common.wire_protocol_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017org.apache.kudu'
  _APPSTATUSPB._serialized_start=117
  _APPSTATUSPB._serialized_end=614
  _APPSTATUSPB_ERRORCODE._serialized_start=213
  _APPSTATUSPB_ERRORCODE._serialized_end=614
  _NODEINSTANCEPB._serialized_start=616
  _NODEINSTANCEPB._serialized_end=680
  _SERVERREGISTRATIONPB._serialized_start=683
  _SERVERREGISTRATIONPB._serialized_end=985
  _SERVERENTRYPB._serialized_start=988
  _SERVERENTRYPB._serialized_end=1257
  _ROWWISEROWBLOCKPB._serialized_start=1259
  _ROWWISEROWBLOCKPB._serialized_end=1352
  _COLUMNARROWBLOCKPB._serialized_start=1355
  _COLUMNARROWBLOCKPB._serialized_end=1537
  _COLUMNARROWBLOCKPB_COLUMN._serialized_start=1445
  _COLUMNARROWBLOCKPB_COLUMN._serialized_end=1537
# @@protoc_insertion_point(module_scope)
