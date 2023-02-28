# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kudu/util/maintenance_manager.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='kudu/util/maintenance_manager.proto',
  package='kudu',
  syntax='proto2',
  serialized_options=b'\n\017org.apache.kudu',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#kudu/util/maintenance_manager.proto\x12\x04kudu\"\x9b\x04\n\x1aMaintenanceManagerStatusPB\x12O\n\x15registered_operations\x18\x01 \x03(\x0b\x32\x30.kudu.MaintenanceManagerStatusPB.MaintenanceOpPB\x12I\n\x12running_operations\x18\x02 \x03(\x0b\x32-.kudu.MaintenanceManagerStatusPB.OpInstancePB\x12K\n\x14\x63ompleted_operations\x18\x03 \x03(\x0b\x32-.kudu.MaintenanceManagerStatusPB.OpInstancePB\x1a\xad\x01\n\x0fMaintenanceOpPB\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0f\n\x07running\x18\x02 \x02(\r\x12\x10\n\x08runnable\x18\x03 \x02(\x08\x12\x1a\n\x12ram_anchored_bytes\x18\x04 \x02(\x03\x12\x1b\n\x13logs_retained_bytes\x18\x05 \x02(\x03\x12\x18\n\x10perf_improvement\x18\x06 \x02(\x01\x12\x16\n\x0eworkload_score\x18\x07 \x02(\x01\x1a\x64\n\x0cOpInstancePB\x12\x11\n\tthread_id\x18\x01 \x02(\x03\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x17\n\x0f\x64uration_millis\x18\x03 \x01(\x05\x12\x1a\n\x12millis_since_start\x18\x04 \x02(\x05\x42\x11\n\x0forg.apache.kudu'
)




_MAINTENANCEMANAGERSTATUSPB_MAINTENANCEOPPB = _descriptor.Descriptor(
  name='MaintenanceOpPB',
  full_name='kudu.MaintenanceManagerStatusPB.MaintenanceOpPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='kudu.MaintenanceManagerStatusPB.MaintenanceOpPB.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='running', full_name='kudu.MaintenanceManagerStatusPB.MaintenanceOpPB.running', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='runnable', full_name='kudu.MaintenanceManagerStatusPB.MaintenanceOpPB.runnable', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ram_anchored_bytes', full_name='kudu.MaintenanceManagerStatusPB.MaintenanceOpPB.ram_anchored_bytes', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logs_retained_bytes', full_name='kudu.MaintenanceManagerStatusPB.MaintenanceOpPB.logs_retained_bytes', index=4,
      number=5, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='perf_improvement', full_name='kudu.MaintenanceManagerStatusPB.MaintenanceOpPB.perf_improvement', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='workload_score', full_name='kudu.MaintenanceManagerStatusPB.MaintenanceOpPB.workload_score', index=6,
      number=7, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=310,
  serialized_end=483,
)

_MAINTENANCEMANAGERSTATUSPB_OPINSTANCEPB = _descriptor.Descriptor(
  name='OpInstancePB',
  full_name='kudu.MaintenanceManagerStatusPB.OpInstancePB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='thread_id', full_name='kudu.MaintenanceManagerStatusPB.OpInstancePB.thread_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='kudu.MaintenanceManagerStatusPB.OpInstancePB.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duration_millis', full_name='kudu.MaintenanceManagerStatusPB.OpInstancePB.duration_millis', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='millis_since_start', full_name='kudu.MaintenanceManagerStatusPB.OpInstancePB.millis_since_start', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=485,
  serialized_end=585,
)

_MAINTENANCEMANAGERSTATUSPB = _descriptor.Descriptor(
  name='MaintenanceManagerStatusPB',
  full_name='kudu.MaintenanceManagerStatusPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='registered_operations', full_name='kudu.MaintenanceManagerStatusPB.registered_operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='running_operations', full_name='kudu.MaintenanceManagerStatusPB.running_operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='completed_operations', full_name='kudu.MaintenanceManagerStatusPB.completed_operations', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_MAINTENANCEMANAGERSTATUSPB_MAINTENANCEOPPB, _MAINTENANCEMANAGERSTATUSPB_OPINSTANCEPB, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=585,
)

_MAINTENANCEMANAGERSTATUSPB_MAINTENANCEOPPB.containing_type = _MAINTENANCEMANAGERSTATUSPB
_MAINTENANCEMANAGERSTATUSPB_OPINSTANCEPB.containing_type = _MAINTENANCEMANAGERSTATUSPB
_MAINTENANCEMANAGERSTATUSPB.fields_by_name['registered_operations'].message_type = _MAINTENANCEMANAGERSTATUSPB_MAINTENANCEOPPB
_MAINTENANCEMANAGERSTATUSPB.fields_by_name['running_operations'].message_type = _MAINTENANCEMANAGERSTATUSPB_OPINSTANCEPB
_MAINTENANCEMANAGERSTATUSPB.fields_by_name['completed_operations'].message_type = _MAINTENANCEMANAGERSTATUSPB_OPINSTANCEPB
DESCRIPTOR.message_types_by_name['MaintenanceManagerStatusPB'] = _MAINTENANCEMANAGERSTATUSPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MaintenanceManagerStatusPB = _reflection.GeneratedProtocolMessageType('MaintenanceManagerStatusPB', (_message.Message,), {

  'MaintenanceOpPB' : _reflection.GeneratedProtocolMessageType('MaintenanceOpPB', (_message.Message,), {
    'DESCRIPTOR' : _MAINTENANCEMANAGERSTATUSPB_MAINTENANCEOPPB,
    '__module__' : 'kudu.util.maintenance_manager_pb2'
    # @@protoc_insertion_point(class_scope:kudu.MaintenanceManagerStatusPB.MaintenanceOpPB)
    })
  ,

  'OpInstancePB' : _reflection.GeneratedProtocolMessageType('OpInstancePB', (_message.Message,), {
    'DESCRIPTOR' : _MAINTENANCEMANAGERSTATUSPB_OPINSTANCEPB,
    '__module__' : 'kudu.util.maintenance_manager_pb2'
    # @@protoc_insertion_point(class_scope:kudu.MaintenanceManagerStatusPB.OpInstancePB)
    })
  ,
  'DESCRIPTOR' : _MAINTENANCEMANAGERSTATUSPB,
  '__module__' : 'kudu.util.maintenance_manager_pb2'
  # @@protoc_insertion_point(class_scope:kudu.MaintenanceManagerStatusPB)
  })
_sym_db.RegisterMessage(MaintenanceManagerStatusPB)
_sym_db.RegisterMessage(MaintenanceManagerStatusPB.MaintenanceOpPB)
_sym_db.RegisterMessage(MaintenanceManagerStatusPB.OpInstancePB)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)