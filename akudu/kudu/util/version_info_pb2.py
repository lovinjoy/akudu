# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: akudu/kudu/util/version_info.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"akudu/kudu/util/version_info.proto\x12\x04kudu\"\xc2\x01\n\rVersionInfoPB\x12\x10\n\x08git_hash\x18\x01 \x01(\t\x12\x16\n\x0e\x62uild_hostname\x18\x02 \x01(\t\x12\x17\n\x0f\x62uild_timestamp\x18\x03 \x01(\t\x12\x16\n\x0e\x62uild_username\x18\x04 \x01(\t\x12\x18\n\x10\x62uild_clean_repo\x18\x05 \x01(\x08\x12\x10\n\x08\x62uild_id\x18\x06 \x01(\t\x12\x12\n\nbuild_type\x18\x07 \x01(\t\x12\x16\n\x0eversion_string\x18\x08 \x01(\tB\x11\n\x0forg.apache.kudu')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akudu.kudu.util.version_info_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017org.apache.kudu'
  _VERSIONINFOPB._serialized_start=45
  _VERSIONINFOPB._serialized_end=239
# @@protoc_insertion_point(module_scope)
