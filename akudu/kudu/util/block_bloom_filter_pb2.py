# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: akudu/kudu/util/block_bloom_filter.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from akudu.kudu.util import hash_pb2 as akudu_dot_kudu_dot_util_dot_hash__pb2
from akudu.kudu.util import pb_util_pb2 as akudu_dot_kudu_dot_util_dot_pb__util__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(akudu/kudu/util/block_bloom_filter.proto\x12\x04kudu\x1a\x1a\x61kudu/kudu/util/hash.proto\x1a\x1d\x61kudu/kudu/util/pb_util.proto\"\xab\x01\n\x12\x42lockBloomFilterPB\x12\x17\n\x0flog_space_bytes\x18\x01 \x01(\x05\x12\x18\n\nbloom_data\x18\x02 \x01(\x0c\x42\x04\x88\xb5\x18\x01\x12\x14\n\x0c\x61lways_false\x18\x03 \x01(\x08\x12\x36\n\x0ehash_algorithm\x18\x04 \x01(\x0e\x32\x13.kudu.HashAlgorithm:\tFAST_HASH\x12\x14\n\thash_seed\x18\x05 \x01(\r:\x01\x30\x42\x11\n\x0forg.apache.kudu')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akudu.kudu.util.block_bloom_filter_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017org.apache.kudu'
  _BLOCKBLOOMFILTERPB.fields_by_name['bloom_data']._options = None
  _BLOCKBLOOMFILTERPB.fields_by_name['bloom_data']._serialized_options = b'\210\265\030\001'
  _BLOCKBLOOMFILTERPB._serialized_start=110
  _BLOCKBLOOMFILTERPB._serialized_end=281
# @@protoc_insertion_point(module_scope)
