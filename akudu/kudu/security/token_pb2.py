# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: akudu/kudu/security/token.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from akudu.kudu.util import pb_util_pb2 as akudu_dot_kudu_dot_util_dot_pb__util__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x61kudu/kudu/security/token.proto\x12\rkudu.security\x1a\x1d\x61kudu/kudu/util/pb_util.proto\"+\n\x11\x43olumnPrivilegePB\x12\x16\n\x0escan_privilege\x18\x01 \x01(\x08\"\xb7\x02\n\x10TablePrivilegePB\x12\x10\n\x08table_id\x18\x01 \x01(\t\x12\x16\n\x0escan_privilege\x18\x02 \x01(\x08\x12\x18\n\x10insert_privilege\x18\x03 \x01(\x08\x12\x18\n\x10update_privilege\x18\x04 \x01(\x08\x12\x18\n\x10\x64\x65lete_privilege\x18\x05 \x01(\x08\x12P\n\x11\x63olumn_privileges\x18\x06 \x03(\x0b\x32\x35.kudu.security.TablePrivilegePB.ColumnPrivilegesEntry\x1aY\n\x15\x43olumnPrivilegesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .kudu.security.ColumnPrivilegePB:\x02\x38\x01\" \n\x0c\x41uthnTokenPB\x12\x10\n\x08username\x18\x01 \x01(\t\"Z\n\x0c\x41uthzTokenPB\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x38\n\x0ftable_privilege\x18\x02 \x01(\x0b\x32\x1f.kudu.security.TablePrivilegePB\"\xd4\x01\n\x07TokenPB\x12!\n\x19\x65xpire_unix_epoch_seconds\x18\x01 \x01(\x03\x12\x1d\n\x15incompatible_features\x18\x02 \x03(\x05\x12,\n\x05\x61uthn\x18\x03 \x01(\x0b\x32\x1b.kudu.security.AuthnTokenPBH\x00\x12,\n\x05\x61uthz\x18\x04 \x01(\x0b\x32\x1b.kudu.security.AuthzTokenPBH\x00\"\"\n\x07\x46\x65\x61ture\x12\x17\n\x12UNUSED_PLACEHOLDER\x10\xe7\x07\x42\x07\n\x05token\"\x1c\n\x08JwtRawPB\x12\x10\n\x08jwt_data\x18\x01 \x01(\x0c\"Y\n\rSignedTokenPB\x12\x12\n\ntoken_data\x18\x01 \x01(\x0c\x12\x17\n\tsignature\x18\x02 \x01(\x0c\x42\x04\x88\xb5\x18\x01\x12\x1b\n\x13signing_key_seq_num\x18\x03 \x01(\x03\"m\n\x18TokenSigningPrivateKeyPB\x12\x13\n\x0bkey_seq_num\x18\x01 \x01(\x03\x12\x19\n\x0brsa_key_der\x18\x02 \x01(\x0c\x42\x04\x88\xb5\x18\x01\x12!\n\x19\x65xpire_unix_epoch_seconds\x18\x03 \x01(\x03\"f\n\x17TokenSigningPublicKeyPB\x12\x13\n\x0bkey_seq_num\x18\x01 \x01(\x03\x12\x13\n\x0brsa_key_der\x18\x02 \x01(\x0c\x12!\n\x19\x65xpire_unix_epoch_seconds\x18\x03 \x01(\x03\x42\x1a\n\x18org.apache.kudu.security')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akudu.kudu.security.token_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030org.apache.kudu.security'
  _TABLEPRIVILEGEPB_COLUMNPRIVILEGESENTRY._options = None
  _TABLEPRIVILEGEPB_COLUMNPRIVILEGESENTRY._serialized_options = b'8\001'
  _SIGNEDTOKENPB.fields_by_name['signature']._options = None
  _SIGNEDTOKENPB.fields_by_name['signature']._serialized_options = b'\210\265\030\001'
  _TOKENSIGNINGPRIVATEKEYPB.fields_by_name['rsa_key_der']._options = None
  _TOKENSIGNINGPRIVATEKEYPB.fields_by_name['rsa_key_der']._serialized_options = b'\210\265\030\001'
  _COLUMNPRIVILEGEPB._serialized_start=81
  _COLUMNPRIVILEGEPB._serialized_end=124
  _TABLEPRIVILEGEPB._serialized_start=127
  _TABLEPRIVILEGEPB._serialized_end=438
  _TABLEPRIVILEGEPB_COLUMNPRIVILEGESENTRY._serialized_start=349
  _TABLEPRIVILEGEPB_COLUMNPRIVILEGESENTRY._serialized_end=438
  _AUTHNTOKENPB._serialized_start=440
  _AUTHNTOKENPB._serialized_end=472
  _AUTHZTOKENPB._serialized_start=474
  _AUTHZTOKENPB._serialized_end=564
  _TOKENPB._serialized_start=567
  _TOKENPB._serialized_end=779
  _TOKENPB_FEATURE._serialized_start=736
  _TOKENPB_FEATURE._serialized_end=770
  _JWTRAWPB._serialized_start=781
  _JWTRAWPB._serialized_end=809
  _SIGNEDTOKENPB._serialized_start=811
  _SIGNEDTOKENPB._serialized_end=900
  _TOKENSIGNINGPRIVATEKEYPB._serialized_start=902
  _TOKENSIGNINGPRIVATEKEYPB._serialized_end=1011
  _TOKENSIGNINGPUBLICKEYPB._serialized_start=1013
  _TOKENSIGNINGPUBLICKEYPB._serialized_end=1115
# @@protoc_insertion_point(module_scope)