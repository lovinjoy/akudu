# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: akudu/kudu/tablet/metadata.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from akudu.kudu.common import common_pb2 as akudu_dot_kudu_dot_common_dot_common__pb2
from akudu.kudu.consensus import opid_pb2 as akudu_dot_kudu_dot_consensus_dot_opid__pb2
from akudu.kudu.fs import fs_pb2 as akudu_dot_kudu_dot_fs_dot_fs__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n akudu/kudu/tablet/metadata.proto\x12\x0bkudu.tablet\x1a\x1e\x61kudu/kudu/common/common.proto\x1a\x1f\x61kudu/kudu/consensus/opid.proto\x1a\x16\x61kudu/kudu/fs/fs.proto\"A\n\x0c\x43olumnDataPB\x12\x1e\n\x05\x62lock\x18\x02 \x02(\x0b\x32\x0f.kudu.BlockIdPB\x12\x11\n\tcolumn_id\x18\x04 \x01(\x05\"-\n\x0b\x44\x65ltaDataPB\x12\x1e\n\x05\x62lock\x18\x02 \x02(\x0b\x32\x0f.kudu.BlockIdPB\"\xdd\x02\n\x0cRowSetDataPB\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x1b\n\x13last_durable_dms_id\x18\x02 \x02(\x03\x12*\n\x07\x63olumns\x18\x03 \x03(\x0b\x32\x19.kudu.tablet.ColumnDataPB\x12-\n\x0bredo_deltas\x18\x04 \x03(\x0b\x32\x18.kudu.tablet.DeltaDataPB\x12-\n\x0bundo_deltas\x18\x05 \x03(\x0b\x32\x18.kudu.tablet.DeltaDataPB\x12$\n\x0b\x62loom_block\x18\x06 \x01(\x0b\x32\x0f.kudu.BlockIdPB\x12*\n\x11\x61\x64hoc_index_block\x18\x07 \x01(\x0b\x32\x0f.kudu.BlockIdPB\x12\x17\n\x0fmin_encoded_key\x18\x08 \x01(\x0c\x12\x17\n\x0fmax_encoded_key\x18\t \x01(\x0c\x12\x16\n\x0elive_row_count\x18\n \x01(\x03\"{\n\rTxnMetadataPB\x12\x0f\n\x07\x61\x62orted\x18\x01 \x01(\x08\x12\x18\n\x10\x63ommit_timestamp\x18\x02 \x01(\x03\x12 \n\x18\x63ommit_mvcc_op_timestamp\x18\x03 \x01(\x03\x12\x1d\n\x15\x66lushed_committed_mrs\x18\x04 \x01(\x08\"\xd4\x06\n\x12TabletSuperBlockPB\x12\x10\n\x08table_id\x18\x01 \x02(\x0c\x12\x11\n\ttablet_id\x18\x02 \x02(\x0c\x12%\n\ntable_type\x18\x13 \x01(\x0e\x32\x11.kudu.TableTypePB\x12\x1b\n\x13last_durable_mrs_id\x18\x03 \x02(\x03\x12\x11\n\tstart_key\x18\x04 \x01(\x0c\x12\x0f\n\x07\x65nd_key\x18\x05 \x01(\x0c\x12$\n\tpartition\x18\r \x01(\x0b\x32\x11.kudu.PartitionPB\x12*\n\x07rowsets\x18\x06 \x03(\x0b\x32\x19.kudu.tablet.RowSetDataPB\x12\x12\n\ntable_name\x18\x07 \x02(\t\x12\x1e\n\x06schema\x18\x08 \x02(\x0b\x32\x0e.kudu.SchemaPB\x12\x16\n\x0eschema_version\x18\t \x02(\r\x12\x31\n\x10partition_schema\x18\x0e \x01(\x0b\x32\x17.kudu.PartitionSchemaPB\x12L\n\x11tablet_data_state\x18\n \x01(\x0e\x32\x1c.kudu.tablet.TabletDataState:\x13TABLET_DATA_UNKNOWN\x12(\n\x0forphaned_blocks\x18\x0b \x03(\x0b\x32\x0f.kudu.BlockIdPB\x12\x38\n\x1atombstone_last_logged_opid\x18\x0c \x01(\x0b\x32\x14.kudu.consensus.OpId\x12,\n\x0e\x64\x61ta_dir_group\x18\x0f \x01(\x0b\x32\x14.kudu.DataDirGroupPB\x12\x1f\n\x17supports_live_row_count\x18\x10 \x01(\x08\x12.\n\x0c\x65xtra_config\x18\x11 \x01(\x0b\x32\x18.kudu.TableExtraConfigPB\x12\x17\n\x0f\x64imension_label\x18\x12 \x01(\t\x12\x46\n\x0ctxn_metadata\x18\x14 \x03(\x0b\x32\x30.kudu.tablet.TabletSuperBlockPB.TxnMetadataEntry\x1aN\n\x10TxnMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.kudu.tablet.TxnMetadataPB:\x02\x38\x01\"E\n\x15ReportedTabletStatsPB\x12\x14\n\x0con_disk_size\x18\x01 \x01(\x04\x12\x16\n\x0elive_row_count\x18\x02 \x01(\x04*\x90\x01\n\x0fTabletDataState\x12\x18\n\x13TABLET_DATA_UNKNOWN\x10\xe7\x07\x12\x17\n\x13TABLET_DATA_COPYING\x10\x00\x12\x15\n\x11TABLET_DATA_READY\x10\x01\x12\x17\n\x13TABLET_DATA_DELETED\x10\x02\x12\x1a\n\x16TABLET_DATA_TOMBSTONED\x10\x03*\x98\x01\n\rTabletStatePB\x12\x0c\n\x07UNKNOWN\x10\xe7\x07\x12\x13\n\x0fNOT_INITIALIZED\x10\x06\x12\x0f\n\x0bINITIALIZED\x10\x05\x12\x11\n\rBOOTSTRAPPING\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02\x12\x0c\n\x08STOPPING\x10\x03\x12\x0b\n\x07STOPPED\x10\x07\x12\x0c\n\x08SHUTDOWN\x10\x04\x42\x18\n\x16org.apache.kudu.tablet')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akudu.kudu.tablet.metadata_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026org.apache.kudu.tablet'
  _TABLETSUPERBLOCKPB_TXNMETADATAENTRY._options = None
  _TABLETSUPERBLOCKPB_TXNMETADATAENTRY._serialized_options = b'8\001'
  _TABLETDATASTATE._serialized_start=1656
  _TABLETDATASTATE._serialized_end=1800
  _TABLETSTATEPB._serialized_start=1803
  _TABLETSTATEPB._serialized_end=1955
  _COLUMNDATAPB._serialized_start=138
  _COLUMNDATAPB._serialized_end=203
  _DELTADATAPB._serialized_start=205
  _DELTADATAPB._serialized_end=250
  _ROWSETDATAPB._serialized_start=253
  _ROWSETDATAPB._serialized_end=602
  _TXNMETADATAPB._serialized_start=604
  _TXNMETADATAPB._serialized_end=727
  _TABLETSUPERBLOCKPB._serialized_start=730
  _TABLETSUPERBLOCKPB._serialized_end=1582
  _TABLETSUPERBLOCKPB_TXNMETADATAENTRY._serialized_start=1504
  _TABLETSUPERBLOCKPB_TXNMETADATAENTRY._serialized_end=1582
  _REPORTEDTABLETSTATSPB._serialized_start=1584
  _REPORTEDTABLETSTATSPB._serialized_end=1653
# @@protoc_insertion_point(module_scope)