# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: akudu/kudu/util/mem_tracker.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!akudu/kudu/util/mem_tracker.proto\x12\x04kudu\"\x9f\x01\n\x0cMemTrackerPB\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tparent_id\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x03\x12\x1b\n\x13\x63urrent_consumption\x18\x04 \x01(\x03\x12\x18\n\x10peak_consumption\x18\x05 \x01(\x03\x12*\n\x0e\x63hild_trackers\x18\x06 \x03(\x0b\x32\x12.kudu.MemTrackerPBB\x11\n\x0forg.apache.kudu')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akudu.kudu.util.mem_tracker_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017org.apache.kudu'
  _MEMTRACKERPB._serialized_start=44
  _MEMTRACKERPB._serialized_end=203
# @@protoc_insertion_point(module_scope)
