# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/components/calculators/classification_aggregation_calculator.proto
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
  name='mediapipe/tasks/cc/components/calculators/classification_aggregation_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nUmediapipe/tasks/cc/components/calculators/classification_aggregation_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xa6\x01\n*ClassificationAggregationCalculatorOptions\x12\x12\n\nhead_names\x18\x01 \x03(\t2d\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xf8\x8e\xf5\xd5\x01 \x01(\x0b\x32\x35.mediapipe.ClassificationAggregationCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_CLASSIFICATIONAGGREGATIONCALCULATOROPTIONS = _descriptor.Descriptor(
  name='ClassificationAggregationCalculatorOptions',
  full_name='mediapipe.ClassificationAggregationCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='head_names', full_name='mediapipe.ClassificationAggregationCalculatorOptions.head_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.ClassificationAggregationCalculatorOptions.ext', index=0,
      number=448612216, type=11, cpp_type=10, label=1,
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
  serialized_start=139,
  serialized_end=305,
)

DESCRIPTOR.message_types_by_name['ClassificationAggregationCalculatorOptions'] = _CLASSIFICATIONAGGREGATIONCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClassificationAggregationCalculatorOptions = _reflection.GeneratedProtocolMessageType('ClassificationAggregationCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFICATIONAGGREGATIONCALCULATOROPTIONS,
  '__module__' : 'mediapipe.tasks.cc.components.calculators.classification_aggregation_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.ClassificationAggregationCalculatorOptions)
  })
_sym_db.RegisterMessage(ClassificationAggregationCalculatorOptions)

_CLASSIFICATIONAGGREGATIONCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _CLASSIFICATIONAGGREGATIONCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_CLASSIFICATIONAGGREGATIONCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
