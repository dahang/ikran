# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import sync_pb2
import extension_setting_specifics_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='app_setting_specifics.proto',
  package='sync_pb',
  serialized_pb='\n\x1b\x61pp_setting_specifics.proto\x12\x07sync_pb\x1a\nsync.proto\x1a!extension_setting_specifics.proto\"T\n\x13\x41ppSettingSpecifics\x12=\n\x11\x65xtension_setting\x18\x01 \x01(\x0b\x32\".sync_pb.ExtensionSettingSpecifics:M\n\x0b\x61pp_setting\x12\x18.sync_pb.EntitySpecifics\x18\xe8\xa9\x06 \x01(\x0b\x32\x1c.sync_pb.AppSettingSpecificsB\x04H\x03X\x01')


APP_SETTING_FIELD_NUMBER = 103656
app_setting = descriptor.FieldDescriptor(
  name='app_setting', full_name='sync_pb.app_setting', index=0,
  number=103656, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_APPSETTINGSPECIFICS = descriptor.Descriptor(
  name='AppSettingSpecifics',
  full_name='sync_pb.AppSettingSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='extension_setting', full_name='sync_pb.AppSettingSpecifics.extension_setting', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=87,
  serialized_end=171,
)

_APPSETTINGSPECIFICS.fields_by_name['extension_setting'].message_type = extension_setting_specifics_pb2._EXTENSIONSETTINGSPECIFICS
DESCRIPTOR.message_types_by_name['AppSettingSpecifics'] = _APPSETTINGSPECIFICS

class AppSettingSpecifics(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _APPSETTINGSPECIFICS
  
  # @@protoc_insertion_point(class_scope:sync_pb.AppSettingSpecifics)

app_setting.message_type = _APPSETTINGSPECIFICS
sync_pb2.EntitySpecifics.RegisterExtension(app_setting)
# @@protoc_insertion_point(module_scope)