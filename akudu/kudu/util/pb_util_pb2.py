# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: akudu/kudu/util/pb_util.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61kudu/kudu/util/pb_util.proto\x12\x04kudu\x1a google/protobuf/descriptor.proto\"[\n\x14\x43ontainerSupHeaderPB\x12\x32\n\x06protos\x18\x01 \x02(\x0b\x32\".google.protobuf.FileDescriptorSet\x12\x0f\n\x07pb_type\x18\x02 \x02(\t:6\n\x06REDACT\x12\x1d.google.protobuf.FieldOptions\x18\xd1\x86\x03 \x01(\x08:\x05\x66\x61lseB\x11\n\x0forg.apache.kudu')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akudu.kudu.util.pb_util_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(REDACT)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017org.apache.kudu'
  _CONTAINERSUPHEADERPB._serialized_start=73
  _CONTAINERSUPHEADERPB._serialized_end=164
# @@protoc_insertion_point(module_scope)