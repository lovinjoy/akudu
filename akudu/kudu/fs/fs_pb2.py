# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: akudu/kudu/fs/fs.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61kudu/kudu/fs/fs.proto\x12\x04kudu\"\x7f\n\x12InstanceMetadataPB\x12\x0c\n\x04uuid\x18\x01 \x02(\x0c\x12\x14\n\x0c\x66ormat_stamp\x18\x02 \x02(\t\x12\x12\n\nserver_key\x18\x03 \x01(\t\x12\x15\n\rserver_key_iv\x18\x04 \x01(\t\x12\x1a\n\x12server_key_version\x18\x05 \x01(\t\"+\n\x08\x44irSetPB\x12\x0c\n\x04uuid\x18\x01 \x02(\x0c\x12\x11\n\tall_uuids\x18\x02 \x03(\x0c\"o\n\x15\x44irInstanceMetadataPB\x12\x1f\n\x07\x64ir_set\x18\x01 \x02(\x0b\x32\x0e.kudu.DirSetPB\x12\x10\n\x08\x64ir_type\x18\x02 \x02(\t\x12#\n\x1b\x66ilesystem_block_size_bytes\x18\x03 \x01(\x04\"\x17\n\tBlockIdPB\x12\n\n\x02id\x18\x01 \x02(\x06\"\x90\x01\n\rBlockRecordPB\x12!\n\x08\x62lock_id\x18\x01 \x02(\x0b\x32\x0f.kudu.BlockIdPB\x12&\n\x07op_type\x18\x02 \x02(\x0e\x32\x15.kudu.BlockRecordType\x12\x14\n\x0ctimestamp_us\x18\x03 \x02(\x04\x12\x0e\n\x06offset\x18\x04 \x01(\x03\x12\x0e\n\x06length\x18\x05 \x01(\x03\"\x1f\n\x0e\x44\x61taDirGroupPB\x12\r\n\x05uuids\x18\x01 \x03(\x0c*6\n\x0f\x42lockRecordType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x43REATE\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\x42\x11\n\x0forg.apache.kudu')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akudu.kudu.fs.fs_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017org.apache.kudu'
  _BLOCKRECORDTYPE._serialized_start=524
  _BLOCKRECORDTYPE._serialized_end=578
  _INSTANCEMETADATAPB._serialized_start=32
  _INSTANCEMETADATAPB._serialized_end=159
  _DIRSETPB._serialized_start=161
  _DIRSETPB._serialized_end=204
  _DIRINSTANCEMETADATAPB._serialized_start=206
  _DIRINSTANCEMETADATAPB._serialized_end=317
  _BLOCKIDPB._serialized_start=319
  _BLOCKIDPB._serialized_end=342
  _BLOCKRECORDPB._serialized_start=345
  _BLOCKRECORDPB._serialized_end=489
  _DATADIRGROUPPB._serialized_start=491
  _DATADIRGROUPPB._serialized_end=522
# @@protoc_insertion_point(module_scope)
