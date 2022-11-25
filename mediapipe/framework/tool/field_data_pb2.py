# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/tool/field_data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/framework/tool/field_data.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)mediapipe/framework/tool/field_data.proto\x12\tmediapipe\".\n\x0bMessageData\x12\x10\n\x08type_url\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"\x96\x02\n\tFieldData\x12\x15\n\x0bint32_value\x18\x01 \x01(\x11H\x00\x12\x15\n\x0bint64_value\x18\x02 \x01(\x12H\x00\x12\x16\n\x0cuint32_value\x18\x03 \x01(\rH\x00\x12\x16\n\x0cuint64_value\x18\x04 \x01(\x04H\x00\x12\x16\n\x0c\x64ouble_value\x18\x05 \x01(\x01H\x00\x12\x15\n\x0b\x66loat_value\x18\x06 \x01(\x02H\x00\x12\x14\n\nbool_value\x18\x07 \x01(\x08H\x00\x12\x14\n\nenum_value\x18\x08 \x01(\x11H\x00\x12\x16\n\x0cstring_value\x18\t \x01(\tH\x00\x12/\n\rmessage_value\x18\n \x01(\x0b\x32\x16.mediapipe.MessageDataH\x00\x42\x07\n\x05value'
)




_MESSAGEDATA = _descriptor.Descriptor(
  name='MessageData',
  full_name='mediapipe.MessageData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type_url', full_name='mediapipe.MessageData.type_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='mediapipe.MessageData.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=56,
  serialized_end=102,
)


_FIELDDATA = _descriptor.Descriptor(
  name='FieldData',
  full_name='mediapipe.FieldData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='int32_value', full_name='mediapipe.FieldData.int32_value', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int64_value', full_name='mediapipe.FieldData.int64_value', index=1,
      number=2, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uint32_value', full_name='mediapipe.FieldData.uint32_value', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uint64_value', full_name='mediapipe.FieldData.uint64_value', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='mediapipe.FieldData.double_value', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='float_value', full_name='mediapipe.FieldData.float_value', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='mediapipe.FieldData.bool_value', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enum_value', full_name='mediapipe.FieldData.enum_value', index=7,
      number=8, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='mediapipe.FieldData.string_value', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message_value', full_name='mediapipe.FieldData.message_value', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='value', full_name='mediapipe.FieldData.value',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=105,
  serialized_end=383,
)

_FIELDDATA.fields_by_name['message_value'].message_type = _MESSAGEDATA
_FIELDDATA.oneofs_by_name['value'].fields.append(
  _FIELDDATA.fields_by_name['int32_value'])
_FIELDDATA.fields_by_name['int32_value'].containing_oneof = _FIELDDATA.oneofs_by_name['value']
_FIELDDATA.oneofs_by_name['value'].fields.append(
  _FIELDDATA.fields_by_name['int64_value'])
_FIELDDATA.fields_by_name['int64_value'].containing_oneof = _FIELDDATA.oneofs_by_name['value']
_FIELDDATA.oneofs_by_name['value'].fields.append(
  _FIELDDATA.fields_by_name['uint32_value'])
_FIELDDATA.fields_by_name['uint32_value'].containing_oneof = _FIELDDATA.oneofs_by_name['value']
_FIELDDATA.oneofs_by_name['value'].fields.append(
  _FIELDDATA.fields_by_name['uint64_value'])
_FIELDDATA.fields_by_name['uint64_value'].containing_oneof = _FIELDDATA.oneofs_by_name['value']
_FIELDDATA.oneofs_by_name['value'].fields.append(
  _FIELDDATA.fields_by_name['double_value'])
_FIELDDATA.fields_by_name['double_value'].containing_oneof = _FIELDDATA.oneofs_by_name['value']
_FIELDDATA.oneofs_by_name['value'].fields.append(
  _FIELDDATA.fields_by_name['float_value'])
_FIELDDATA.fields_by_name['float_value'].containing_oneof = _FIELDDATA.oneofs_by_name['value']
_FIELDDATA.oneofs_by_name['value'].fields.append(
  _FIELDDATA.fields_by_name['bool_value'])
_FIELDDATA.fields_by_name['bool_value'].containing_oneof = _FIELDDATA.oneofs_by_name['value']
_FIELDDATA.oneofs_by_name['value'].fields.append(
  _FIELDDATA.fields_by_name['enum_value'])
_FIELDDATA.fields_by_name['enum_value'].containing_oneof = _FIELDDATA.oneofs_by_name['value']
_FIELDDATA.oneofs_by_name['value'].fields.append(
  _FIELDDATA.fields_by_name['string_value'])
_FIELDDATA.fields_by_name['string_value'].containing_oneof = _FIELDDATA.oneofs_by_name['value']
_FIELDDATA.oneofs_by_name['value'].fields.append(
  _FIELDDATA.fields_by_name['message_value'])
_FIELDDATA.fields_by_name['message_value'].containing_oneof = _FIELDDATA.oneofs_by_name['value']
DESCRIPTOR.message_types_by_name['MessageData'] = _MESSAGEDATA
DESCRIPTOR.message_types_by_name['FieldData'] = _FIELDDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessageData = _reflection.GeneratedProtocolMessageType('MessageData', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEDATA,
  '__module__' : 'mediapipe.framework.tool.field_data_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.MessageData)
  })
_sym_db.RegisterMessage(MessageData)

FieldData = _reflection.GeneratedProtocolMessageType('FieldData', (_message.Message,), {
  'DESCRIPTOR' : _FIELDDATA,
  '__module__' : 'mediapipe.framework.tool.field_data_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.FieldData)
  })
_sym_db.RegisterMessage(FieldData)


# @@protoc_insertion_point(module_scope)
