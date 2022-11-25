# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/text/text_embedder/proto/text_embedder_graph_options.proto
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
from mediapipe.tasks.cc.components.processors.proto import embedder_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_components_dot_processors_dot_proto_dot_embedder__options__pb2
from mediapipe.tasks.cc.core.proto import base_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/tasks/cc/text/text_embedder/proto/text_embedder_graph_options.proto',
  package='mediapipe.tasks.text.text_embedder.proto',
  syntax='proto2',
  serialized_options=b'\n2com.google.mediapipe.tasks.text.textembedder.protoB\035TextEmbedderGraphOptionsProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nMmediapipe/tasks/cc/text/text_embedder/proto/text_embedder_graph_options.proto\x12(mediapipe.tasks.text.text_embedder.proto\x1a$mediapipe/framework/calculator.proto\x1a\x45mediapipe/tasks/cc/components/processors/proto/embedder_options.proto\x1a\x30mediapipe/tasks/cc/core/proto/base_options.proto\"\xa4\x02\n\x18TextEmbedderGraphOptions\x12=\n\x0c\x62\x61se_options\x18\x01 \x01(\x0b\x32\'.mediapipe.tasks.core.proto.BaseOptions\x12V\n\x10\x65mbedder_options\x18\x02 \x01(\x0b\x32<.mediapipe.tasks.components.processors.proto.EmbedderOptions2q\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x84\xe3\xdd\xe3\x01 \x01(\x0b\x32\x42.mediapipe.tasks.text.text_embedder.proto.TextEmbedderGraphOptionsBS\n2com.google.mediapipe.tasks.text.textembedder.protoB\x1dTextEmbedderGraphOptionsProto'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_components_dot_processors_dot_proto_dot_embedder__options__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2.DESCRIPTOR,])




_TEXTEMBEDDERGRAPHOPTIONS = _descriptor.Descriptor(
  name='TextEmbedderGraphOptions',
  full_name='mediapipe.tasks.text.text_embedder.proto.TextEmbedderGraphOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_options', full_name='mediapipe.tasks.text.text_embedder.proto.TextEmbedderGraphOptions.base_options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='embedder_options', full_name='mediapipe.tasks.text.text_embedder.proto.TextEmbedderGraphOptions.embedder_options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.tasks.text.text_embedder.proto.TextEmbedderGraphOptions.ext', index=0,
      number=477589892, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=283,
  serialized_end=575,
)

_TEXTEMBEDDERGRAPHOPTIONS.fields_by_name['base_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2._BASEOPTIONS
_TEXTEMBEDDERGRAPHOPTIONS.fields_by_name['embedder_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_components_dot_processors_dot_proto_dot_embedder__options__pb2._EMBEDDEROPTIONS
DESCRIPTOR.message_types_by_name['TextEmbedderGraphOptions'] = _TEXTEMBEDDERGRAPHOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TextEmbedderGraphOptions = _reflection.GeneratedProtocolMessageType('TextEmbedderGraphOptions', (_message.Message,), {
  'DESCRIPTOR' : _TEXTEMBEDDERGRAPHOPTIONS,
  '__module__' : 'mediapipe.tasks.cc.text.text_embedder.proto.text_embedder_graph_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.text.text_embedder.proto.TextEmbedderGraphOptions)
  })
_sym_db.RegisterMessage(TextEmbedderGraphOptions)

_TEXTEMBEDDERGRAPHOPTIONS.extensions_by_name['ext'].message_type = _TEXTEMBEDDERGRAPHOPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TEXTEMBEDDERGRAPHOPTIONS.extensions_by_name['ext'])

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
