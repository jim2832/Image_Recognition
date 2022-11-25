# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/components/proto/text_preprocessing_graph_options.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/tasks/cc/components/proto/text_preprocessing_graph_options.proto',
  package='mediapipe.tasks.components.proto',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nJmediapipe/tasks/cc/components/proto/text_preprocessing_graph_options.proto\x12 mediapipe.tasks.components.proto\x1a$mediapipe/framework/calculator.proto\"\x8b\x03\n\x1dTextPreprocessingGraphOptions\x12k\n\x11preprocessor_type\x18\x01 \x01(\x0e\x32P.mediapipe.tasks.components.proto.TextPreprocessingGraphOptions.PreprocessorType\x12\x13\n\x0bmax_seq_len\x18\x02 \x01(\x05\"x\n\x10PreprocessorType\x12\x1c\n\x18UNSPECIFIED_PREPROCESSOR\x10\x00\x12\x15\n\x11\x42\x45RT_PREPROCESSOR\x10\x01\x12\x16\n\x12REGEX_PREPROCESSOR\x10\x02\x12\x17\n\x13STRING_PREPROCESSOR\x10\x03\x32n\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xbf\xbc\xb8\xe3\x01 \x01(\x0b\x32?.mediapipe.tasks.components.proto.TextPreprocessingGraphOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])



_TEXTPREPROCESSINGGRAPHOPTIONS_PREPROCESSORTYPE = _descriptor.EnumDescriptor(
  name='PreprocessorType',
  full_name='mediapipe.tasks.components.proto.TextPreprocessingGraphOptions.PreprocessorType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED_PREPROCESSOR', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BERT_PREPROCESSOR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REGEX_PREPROCESSOR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STRING_PREPROCESSOR', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=314,
  serialized_end=434,
)
_sym_db.RegisterEnumDescriptor(_TEXTPREPROCESSINGGRAPHOPTIONS_PREPROCESSORTYPE)


_TEXTPREPROCESSINGGRAPHOPTIONS = _descriptor.Descriptor(
  name='TextPreprocessingGraphOptions',
  full_name='mediapipe.tasks.components.proto.TextPreprocessingGraphOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='preprocessor_type', full_name='mediapipe.tasks.components.proto.TextPreprocessingGraphOptions.preprocessor_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_seq_len', full_name='mediapipe.tasks.components.proto.TextPreprocessingGraphOptions.max_seq_len', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.tasks.components.proto.TextPreprocessingGraphOptions.ext', index=0,
      number=476978751, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  nested_types=[],
  enum_types=[
    _TEXTPREPROCESSINGGRAPHOPTIONS_PREPROCESSORTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=546,
)

_TEXTPREPROCESSINGGRAPHOPTIONS.fields_by_name['preprocessor_type'].enum_type = _TEXTPREPROCESSINGGRAPHOPTIONS_PREPROCESSORTYPE
_TEXTPREPROCESSINGGRAPHOPTIONS_PREPROCESSORTYPE.containing_type = _TEXTPREPROCESSINGGRAPHOPTIONS
DESCRIPTOR.message_types_by_name['TextPreprocessingGraphOptions'] = _TEXTPREPROCESSINGGRAPHOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TextPreprocessingGraphOptions = _reflection.GeneratedProtocolMessageType('TextPreprocessingGraphOptions', (_message.Message,), {
  'DESCRIPTOR' : _TEXTPREPROCESSINGGRAPHOPTIONS,
  '__module__' : 'mediapipe.tasks.cc.components.proto.text_preprocessing_graph_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.components.proto.TextPreprocessingGraphOptions)
  })
_sym_db.RegisterMessage(TextPreprocessingGraphOptions)

_TEXTPREPROCESSINGGRAPHOPTIONS.extensions_by_name['ext'].message_type = _TEXTPREPROCESSINGGRAPHOPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TEXTPREPROCESSINGGRAPHOPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
