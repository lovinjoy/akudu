# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: akudu/kudu/consensus/consensus.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from akudu.kudu.common import common_pb2 as akudu_dot_kudu_dot_common_dot_common__pb2
from akudu.kudu.common import wire_protocol_pb2 as akudu_dot_kudu_dot_common_dot_wire__protocol__pb2
from akudu.kudu.consensus import metadata_pb2 as akudu_dot_kudu_dot_consensus_dot_metadata__pb2
from akudu.kudu.consensus import opid_pb2 as akudu_dot_kudu_dot_consensus_dot_opid__pb2
from akudu.kudu.consensus import replica_management_pb2 as akudu_dot_kudu_dot_consensus_dot_replica__management__pb2
from akudu.kudu.rpc import rpc_header_pb2 as akudu_dot_kudu_dot_rpc_dot_rpc__header__pb2
from akudu.kudu.tablet import metadata_pb2 as akudu_dot_kudu_dot_tablet_dot_metadata__pb2
from akudu.kudu.tablet import tablet_pb2 as akudu_dot_kudu_dot_tablet_dot_tablet__pb2
from akudu.kudu.tserver import tserver_admin_pb2 as akudu_dot_kudu_dot_tserver_dot_tserver__admin__pb2
from akudu.kudu.tserver import tserver_pb2 as akudu_dot_kudu_dot_tserver_dot_tserver__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$akudu/kudu/consensus/consensus.proto\x12\x0ekudu.consensus\x1a\x1e\x61kudu/kudu/common/common.proto\x1a%akudu/kudu/common/wire_protocol.proto\x1a#akudu/kudu/consensus/metadata.proto\x1a\x1f\x61kudu/kudu/consensus/opid.proto\x1a-akudu/kudu/consensus/replica_management.proto\x1a\x1f\x61kudu/kudu/rpc/rpc_header.proto\x1a akudu/kudu/tablet/metadata.proto\x1a\x1e\x61kudu/kudu/tablet/tablet.proto\x1a&akudu/kudu/tserver/tserver_admin.proto\x1a akudu/kudu/tserver/tserver.proto\"\xad\x02\n\x10\x43onsensusErrorPB\x12\x33\n\x04\x63ode\x18\x01 \x02(\x0e\x32%.kudu.consensus.ConsensusErrorPB.Code\x12!\n\x06status\x18\x02 \x02(\x0b\x32\x11.kudu.AppStatusPB\"\xc0\x01\n\x04\x43ode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x10\n\x0cINVALID_TERM\x10\x02\x12\x15\n\x11LAST_OPID_TOO_OLD\x10\x03\x12\x11\n\rALREADY_VOTED\x10\x04\x12\x11\n\rNOT_IN_QUORUM\x10\x05\x12\x1f\n\x1bPRECEDING_ENTRY_DIDNT_MATCH\x10\x06\x12\x13\n\x0fLEADER_IS_ALIVE\x10\x07\x12\x12\n\x0e\x43ONSENSUS_BUSY\x10\x08\x12\x12\n\x0e\x43\x41NNOT_PREPARE\x10\t\"\x8d\x01\n\x14\x43hangeConfigRecordPB\x12\x11\n\ttablet_id\x18\x01 \x02(\x0c\x12\x30\n\nold_config\x18\x02 \x02(\x0b\x32\x1c.kudu.consensus.RaftConfigPB\x12\x30\n\nnew_config\x18\x03 \x02(\x0b\x32\x1c.kudu.consensus.RaftConfigPB\"\xb8\x01\n\x15\x43hangeConfigRequestPB\x12\x11\n\tdest_uuid\x18\x04 \x01(\x0c\x12\x11\n\ttablet_id\x18\x01 \x02(\x0c\x12.\n\x04type\x18\x02 \x01(\x0e\x32 .kudu.consensus.ChangeConfigType\x12*\n\x06server\x18\x03 \x01(\x0b\x32\x1a.kudu.consensus.RaftPeerPB\x12\x1d\n\x15\x63\x61s_config_opid_index\x18\x05 \x01(\x03\"\xa6\x02\n\x19\x42ulkChangeConfigRequestPB\x12\x11\n\tdest_uuid\x18\x01 \x01(\x0c\x12\x11\n\ttablet_id\x18\x02 \x02(\x0c\x12T\n\x0e\x63onfig_changes\x18\x03 \x03(\x0b\x32<.kudu.consensus.BulkChangeConfigRequestPB.ConfigChangeItemPB\x12\x1d\n\x15\x63\x61s_config_opid_index\x18\x04 \x01(\x03\x1an\n\x12\x43onfigChangeItemPB\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .kudu.consensus.ChangeConfigType\x12(\n\x04peer\x18\x02 \x01(\x0b\x32\x1a.kudu.consensus.RaftPeerPB\"\x8d\x01\n\x16\x43hangeConfigResponsePB\x12\x30\n\x05\x65rror\x18\x01 \x01(\x0b\x32!.kudu.tserver.TabletServerErrorPB\x12.\n\nnew_config\x18\x02 \x01(\x0b\x32\x1a.kudu.consensus.RaftPeerPB\x12\x11\n\ttimestamp\x18\x03 \x01(\x06\"\xd0\x03\n\x0cReplicateMsg\x12 \n\x02id\x18\x01 \x02(\x0b\x32\x14.kudu.consensus.OpId\x12\x11\n\ttimestamp\x18\x02 \x02(\x06\x12.\n\x07op_type\x18\x04 \x02(\x0e\x32\x1d.kudu.consensus.OperationType\x12\x33\n\rwrite_request\x18\x05 \x01(\x0b\x32\x1c.kudu.tserver.WriteRequestPB\x12@\n\x14\x61lter_schema_request\x18\x06 \x01(\x0b\x32\".kudu.tserver.AlterSchemaRequestPB\x12\x42\n\x14\x63hange_config_record\x18\x07 \x01(\x0b\x32$.kudu.consensus.ChangeConfigRecordPB\x12?\n\x13participant_request\x18\t \x01(\x0b\x32\".kudu.tserver.ParticipantRequestPB\x12)\n\nrequest_id\x18\x08 \x01(\x0b\x32\x15.kudu.rpc.RequestIdPB\x12\x34\n\x0cnoop_request\x18\xe7\x07 \x01(\x0b\x32\x1d.kudu.consensus.NoOpRequestPB\"\x92\x01\n\tCommitMsg\x12.\n\x07op_type\x18\x01 \x02(\x0e\x32\x1d.kudu.consensus.OperationType\x12,\n\x0e\x63ommited_op_id\x18\x02 \x01(\x0b\x32\x14.kudu.consensus.OpId\x12\'\n\x06result\x18\x03 \x01(\x0b\x32\x17.kudu.tablet.TxResultPB\"K\n\rNoOpRequestPB\x12\x19\n\x11payload_for_tests\x18\x01 \x01(\x0c\x12\x1f\n\x17timestamp_in_opid_order\x18\x02 \x01(\x08\"\xc9\x01\n\x11\x43onsensusStatusPB\x12+\n\rlast_received\x18\x01 \x02(\x0b\x32\x14.kudu.consensus.OpId\x12:\n\x1clast_received_current_leader\x18\x04 \x01(\x0b\x32\x14.kudu.consensus.OpId\x12\x1a\n\x12last_committed_idx\x18\x02 \x01(\x03\x12/\n\x05\x65rror\x18\x03 \x01(\x0b\x32 .kudu.consensus.ConsensusErrorPB\"\xe5\x01\n\rVoteRequestPB\x12\x11\n\tdest_uuid\x18\x06 \x01(\x0c\x12\x11\n\ttablet_id\x18\x01 \x02(\t\x12\x16\n\x0e\x63\x61ndidate_uuid\x18\x02 \x02(\x0c\x12\x16\n\x0e\x63\x61ndidate_term\x18\x03 \x02(\x03\x12;\n\x10\x63\x61ndidate_status\x18\x04 \x02(\x0b\x32!.kudu.consensus.ConsensusStatusPB\x12!\n\x12ignore_live_leader\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x0fis_pre_election\x18\x07 \x01(\x08:\x05\x66\x61lse\"\xc5\x01\n\x0eVoteResponsePB\x12\x16\n\x0eresponder_uuid\x18\x01 \x01(\x0c\x12\x16\n\x0eresponder_term\x18\x02 \x01(\x03\x12\x14\n\x0cvote_granted\x18\x03 \x01(\x08\x12:\n\x0f\x63onsensus_error\x18\xe6\x07 \x01(\x0b\x32 .kudu.consensus.ConsensusErrorPB\x12\x31\n\x05\x65rror\x18\xe7\x07 \x01(\x0b\x32!.kudu.tserver.TabletServerErrorPB\"\xe9\x02\n\x12\x43onsensusRequestPB\x12\x11\n\tdest_uuid\x18\x07 \x01(\x0c\x12\x11\n\ttablet_id\x18\x01 \x02(\t\x12\x13\n\x0b\x63\x61ller_uuid\x18\x02 \x02(\x0c\x12\x13\n\x0b\x63\x61ller_term\x18\x03 \x02(\x03\x12*\n\x0cpreceding_id\x18\x04 \x01(\x0b\x32\x14.kudu.consensus.OpId\x12\x17\n\x0f\x63ommitted_index\x18\x08 \x01(\x03\x12\x38\n\x1a\x44\x45PRECATED_committed_index\x18\x05 \x01(\x0b\x32\x14.kudu.consensus.OpId\x12)\n\x03ops\x18\x06 \x03(\x0b\x32\x1c.kudu.consensus.ReplicateMsg\x12\x1c\n\x14\x61ll_replicated_index\x18\t \x01(\x03\x12\x16\n\x0esafe_timestamp\x18\n \x01(\x06\x12#\n\x1blast_idx_appended_to_leader\x18\x0b \x01(\x03\"\xc5\x01\n\x13\x43onsensusResponsePB\x12\x16\n\x0eresponder_uuid\x18\x01 \x01(\x0c\x12\x16\n\x0eresponder_term\x18\x02 \x01(\x03\x12\x31\n\x06status\x18\x03 \x01(\x0b\x32!.kudu.consensus.ConsensusStatusPB\x12\x18\n\x10server_quiescing\x18\x04 \x01(\x08\x12\x31\n\x05\x65rror\x18\xe7\x07 \x01(\x0b\x32!.kudu.tserver.TabletServerErrorPB\"\xa8\x01\n\nOpStatusPB\x12#\n\x05op_id\x18\x01 \x02(\x0b\x32\x14.kudu.consensus.OpId\x12.\n\x07op_type\x18\x02 \x02(\x0e\x32\x1d.kudu.consensus.OperationType\x12\x1a\n\x12running_for_micros\x18\x03 \x02(\x03\x12\x13\n\x0b\x64\x65scription\x18\x04 \x02(\t\x12\x14\n\x0ctrace_buffer\x18\x06 \x01(\t\"\x1a\n\x18GetNodeInstanceRequestPB\"H\n\x19GetNodeInstanceResponsePB\x12+\n\rnode_instance\x18\x01 \x02(\x0b\x32\x14.kudu.NodeInstancePB\"B\n\x1aRunLeaderElectionRequestPB\x12\x11\n\tdest_uuid\x18\x02 \x01(\x0c\x12\x11\n\ttablet_id\x18\x01 \x02(\x0c\"O\n\x1bRunLeaderElectionResponsePB\x12\x30\n\x05\x65rror\x18\x01 \x01(\x0b\x32!.kudu.tserver.TabletServerErrorPB\"\x8a\x01\n\x17LeaderStepDownRequestPB\x12\x11\n\tdest_uuid\x18\x02 \x01(\x0c\x12\x11\n\ttablet_id\x18\x01 \x02(\x0c\x12\x30\n\x04mode\x18\x03 \x01(\x0e\x32\".kudu.consensus.LeaderStepDownMode\x12\x17\n\x0fnew_leader_uuid\x18\x04 \x01(\x0c\"L\n\x18LeaderStepDownResponsePB\x12\x30\n\x05\x65rror\x18\x01 \x01(\x0b\x32!.kudu.tserver.TabletServerErrorPB\"x\n\x14GetLastOpIdRequestPB\x12\x11\n\tdest_uuid\x18\x02 \x01(\x0c\x12\x11\n\ttablet_id\x18\x01 \x02(\x0c\x12:\n\topid_type\x18\x03 \x01(\x0e\x32\x18.kudu.consensus.OpIdType:\rRECEIVED_OPID\"m\n\x15GetLastOpIdResponsePB\x12\"\n\x04opid\x18\x01 \x01(\x0b\x32\x14.kudu.consensus.OpId\x12\x30\n\x05\x65rror\x18\x02 \x01(\x0b\x32!.kudu.tserver.TabletServerErrorPB\"\x7f\n\x1aGetConsensusStateRequestPB\x12\x11\n\tdest_uuid\x18\x01 \x01(\x0c\x12\x12\n\ntablet_ids\x18\x02 \x03(\x0c\x12:\n\rreport_health\x18\x03 \x01(\x0e\x32#.kudu.consensus.IncludeHealthReport\"\xcb\x02\n\x1bGetConsensusStateResponsePB\x12R\n\x07tablets\x18\x01 \x03(\x0b\x32\x41.kudu.consensus.GetConsensusStateResponsePB.TabletConsensusInfoPB\x12H\n\x17replica_management_info\x18\x03 \x01(\x0b\x32\'.kudu.consensus.ReplicaManagementInfoPB\x12\x30\n\x05\x65rror\x18\x02 \x01(\x0b\x32!.kudu.tserver.TabletServerErrorPB\x1a\\\n\x15TabletConsensusInfoPB\x12\x11\n\ttablet_id\x18\x01 \x02(\x0c\x12\x30\n\x06\x63state\x18\x02 \x01(\x0b\x32 .kudu.consensus.ConsensusStatePB\"\x9b\x01\n\x18StartTabletCopyRequestPB\x12\x11\n\tdest_uuid\x18\x05 \x01(\x0c\x12\x11\n\ttablet_id\x18\x01 \x02(\x0c\x12\x16\n\x0e\x63opy_peer_uuid\x18\x02 \x02(\x0c\x12(\n\x0e\x63opy_peer_addr\x18\x03 \x02(\x0b\x32\x10.kudu.HostPortPB\x12\x17\n\x0b\x63\x61ller_term\x18\x04 \x01(\x03:\x02-1\"M\n\x19StartTabletCopyResponsePB\x12\x30\n\x05\x65rror\x18\x01 \x01(\x0b\x32!.kudu.tserver.TabletServerErrorPB\"\x88\x01\n\x1bUnsafeChangeConfigRequestPB\x12\x11\n\tdest_uuid\x18\x01 \x01(\x0c\x12\x11\n\ttablet_id\x18\x02 \x02(\x0c\x12\x11\n\tcaller_id\x18\x03 \x02(\x0c\x12\x30\n\nnew_config\x18\x04 \x02(\x0b\x32\x1c.kudu.consensus.RaftConfigPB\"P\n\x1cUnsafeChangeConfigResponsePB\x12\x30\n\x05\x65rror\x18\x01 \x01(\x0b\x32!.kudu.tserver.TabletServerErrorPB*w\n\rOperationType\x12\x0e\n\nUNKNOWN_OP\x10\x00\x12\t\n\x05NO_OP\x10\x01\x12\x0c\n\x08WRITE_OP\x10\x03\x12\x13\n\x0f\x41LTER_SCHEMA_OP\x10\x04\x12\x14\n\x10\x43HANGE_CONFIG_OP\x10\x05\x12\x12\n\x0ePARTICIPANT_OP\x10\x06*:\n\nDriverType\x12\x12\n\x0eUNKNOWN_DRIVER\x10\x00\x12\n\n\x06LEADER\x10\x01\x12\x0c\n\x08\x46OLLOWER\x10\x02*V\n\x10\x43hangeConfigType\x12\x12\n\x0eUNKNOWN_CHANGE\x10\x00\x12\x0c\n\x08\x41\x44\x44_PEER\x10\x01\x12\x0f\n\x0bREMOVE_PEER\x10\x02\x12\x0f\n\x0bMODIFY_PEER\x10\x03*.\n\x12LeaderStepDownMode\x12\n\n\x06\x41\x42RUPT\x10\x01\x12\x0c\n\x08GRACEFUL\x10\x02*H\n\x08OpIdType\x12\x15\n\x11UNKNOWN_OPID_TYPE\x10\x00\x12\x11\n\rRECEIVED_OPID\x10\x01\x12\x12\n\x0e\x43OMMITTED_OPID\x10\x02*j\n\x13IncludeHealthReport\x12\x1d\n\x19UNSPECIFIED_HEALTH_REPORT\x10\x00\x12\x19\n\x15\x45XCLUDE_HEALTH_REPORT\x10\x01\x12\x19\n\x15INCLUDE_HEALTH_REPORT\x10\x02\x32\x83\t\n\x10\x43onsensusService\x12Z\n\x0fUpdateConsensus\x12\".kudu.consensus.ConsensusRequestPB\x1a#.kudu.consensus.ConsensusResponsePB\x12U\n\x14RequestConsensusVote\x12\x1d.kudu.consensus.VoteRequestPB\x1a\x1e.kudu.consensus.VoteResponsePB\x12]\n\x0c\x43hangeConfig\x12%.kudu.consensus.ChangeConfigRequestPB\x1a&.kudu.consensus.ChangeConfigResponsePB\x12\x65\n\x10\x42ulkChangeConfig\x12).kudu.consensus.BulkChangeConfigRequestPB\x1a&.kudu.consensus.ChangeConfigResponsePB\x12o\n\x12UnsafeChangeConfig\x12+.kudu.consensus.UnsafeChangeConfigRequestPB\x1a,.kudu.consensus.UnsafeChangeConfigResponsePB\x12\x66\n\x0fGetNodeInstance\x12(.kudu.consensus.GetNodeInstanceRequestPB\x1a).kudu.consensus.GetNodeInstanceResponsePB\x12l\n\x11RunLeaderElection\x12*.kudu.consensus.RunLeaderElectionRequestPB\x1a+.kudu.consensus.RunLeaderElectionResponsePB\x12\x63\n\x0eLeaderStepDown\x12\'.kudu.consensus.LeaderStepDownRequestPB\x1a(.kudu.consensus.LeaderStepDownResponsePB\x12Z\n\x0bGetLastOpId\x12$.kudu.consensus.GetLastOpIdRequestPB\x1a%.kudu.consensus.GetLastOpIdResponsePB\x12l\n\x11GetConsensusState\x12*.kudu.consensus.GetConsensusStateRequestPB\x1a+.kudu.consensus.GetConsensusStateResponsePB\x12\x66\n\x0fStartTabletCopy\x12(.kudu.consensus.StartTabletCopyRequestPB\x1a).kudu.consensus.StartTabletCopyResponsePB\x1a\x18\xba\xb5\x18\x14\x41uthorizeServiceUserB\x1b\n\x19org.apache.kudu.consensus')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akudu.kudu.consensus.consensus_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031org.apache.kudu.consensus'
  _CONSENSUSSERVICE._options = None
  _CONSENSUSSERVICE._serialized_options = b'\272\265\030\024AuthorizeServiceUser'
  _OPERATIONTYPE._serialized_start=5181
  _OPERATIONTYPE._serialized_end=5300
  _DRIVERTYPE._serialized_start=5302
  _DRIVERTYPE._serialized_end=5360
  _CHANGECONFIGTYPE._serialized_start=5362
  _CHANGECONFIGTYPE._serialized_end=5448
  _LEADERSTEPDOWNMODE._serialized_start=5450
  _LEADERSTEPDOWNMODE._serialized_end=5496
  _OPIDTYPE._serialized_start=5498
  _OPIDTYPE._serialized_end=5570
  _INCLUDEHEALTHREPORT._serialized_start=5572
  _INCLUDEHEALTHREPORT._serialized_end=5678
  _CONSENSUSERRORPB._serialized_start=418
  _CONSENSUSERRORPB._serialized_end=719
  _CONSENSUSERRORPB_CODE._serialized_start=527
  _CONSENSUSERRORPB_CODE._serialized_end=719
  _CHANGECONFIGRECORDPB._serialized_start=722
  _CHANGECONFIGRECORDPB._serialized_end=863
  _CHANGECONFIGREQUESTPB._serialized_start=866
  _CHANGECONFIGREQUESTPB._serialized_end=1050
  _BULKCHANGECONFIGREQUESTPB._serialized_start=1053
  _BULKCHANGECONFIGREQUESTPB._serialized_end=1347
  _BULKCHANGECONFIGREQUESTPB_CONFIGCHANGEITEMPB._serialized_start=1237
  _BULKCHANGECONFIGREQUESTPB_CONFIGCHANGEITEMPB._serialized_end=1347
  _CHANGECONFIGRESPONSEPB._serialized_start=1350
  _CHANGECONFIGRESPONSEPB._serialized_end=1491
  _REPLICATEMSG._serialized_start=1494
  _REPLICATEMSG._serialized_end=1958
  _COMMITMSG._serialized_start=1961
  _COMMITMSG._serialized_end=2107
  _NOOPREQUESTPB._serialized_start=2109
  _NOOPREQUESTPB._serialized_end=2184
  _CONSENSUSSTATUSPB._serialized_start=2187
  _CONSENSUSSTATUSPB._serialized_end=2388
  _VOTEREQUESTPB._serialized_start=2391
  _VOTEREQUESTPB._serialized_end=2620
  _VOTERESPONSEPB._serialized_start=2623
  _VOTERESPONSEPB._serialized_end=2820
  _CONSENSUSREQUESTPB._serialized_start=2823
  _CONSENSUSREQUESTPB._serialized_end=3184
  _CONSENSUSRESPONSEPB._serialized_start=3187
  _CONSENSUSRESPONSEPB._serialized_end=3384
  _OPSTATUSPB._serialized_start=3387
  _OPSTATUSPB._serialized_end=3555
  _GETNODEINSTANCEREQUESTPB._serialized_start=3557
  _GETNODEINSTANCEREQUESTPB._serialized_end=3583
  _GETNODEINSTANCERESPONSEPB._serialized_start=3585
  _GETNODEINSTANCERESPONSEPB._serialized_end=3657
  _RUNLEADERELECTIONREQUESTPB._serialized_start=3659
  _RUNLEADERELECTIONREQUESTPB._serialized_end=3725
  _RUNLEADERELECTIONRESPONSEPB._serialized_start=3727
  _RUNLEADERELECTIONRESPONSEPB._serialized_end=3806
  _LEADERSTEPDOWNREQUESTPB._serialized_start=3809
  _LEADERSTEPDOWNREQUESTPB._serialized_end=3947
  _LEADERSTEPDOWNRESPONSEPB._serialized_start=3949
  _LEADERSTEPDOWNRESPONSEPB._serialized_end=4025
  _GETLASTOPIDREQUESTPB._serialized_start=4027
  _GETLASTOPIDREQUESTPB._serialized_end=4147
  _GETLASTOPIDRESPONSEPB._serialized_start=4149
  _GETLASTOPIDRESPONSEPB._serialized_end=4258
  _GETCONSENSUSSTATEREQUESTPB._serialized_start=4260
  _GETCONSENSUSSTATEREQUESTPB._serialized_end=4387
  _GETCONSENSUSSTATERESPONSEPB._serialized_start=4390
  _GETCONSENSUSSTATERESPONSEPB._serialized_end=4721
  _GETCONSENSUSSTATERESPONSEPB_TABLETCONSENSUSINFOPB._serialized_start=4629
  _GETCONSENSUSSTATERESPONSEPB_TABLETCONSENSUSINFOPB._serialized_end=4721
  _STARTTABLETCOPYREQUESTPB._serialized_start=4724
  _STARTTABLETCOPYREQUESTPB._serialized_end=4879
  _STARTTABLETCOPYRESPONSEPB._serialized_start=4881
  _STARTTABLETCOPYRESPONSEPB._serialized_end=4958
  _UNSAFECHANGECONFIGREQUESTPB._serialized_start=4961
  _UNSAFECHANGECONFIGREQUESTPB._serialized_end=5097
  _UNSAFECHANGECONFIGRESPONSEPB._serialized_start=5099
  _UNSAFECHANGECONFIGRESPONSEPB._serialized_end=5179
  _CONSENSUSSERVICE._serialized_start=5681
  _CONSENSUSSERVICE._serialized_end=6836
# @@protoc_insertion_point(module_scope)
