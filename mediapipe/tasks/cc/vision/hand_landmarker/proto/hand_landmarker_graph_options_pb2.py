# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/vision/hand_landmarker/proto/hand_landmarker_graph_options.proto
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
from mediapipe.tasks.cc.core.proto import base_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2
from mediapipe.tasks.cc.vision.hand_detector.proto import hand_detector_graph_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_vision_dot_hand__detector_dot_proto_dot_hand__detector__graph__options__pb2
from mediapipe.tasks.cc.vision.hand_landmarker.proto import hand_landmarks_detector_graph_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_vision_dot_hand__landmarker_dot_proto_dot_hand__landmarks__detector__graph__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/tasks/cc/vision/hand_landmarker/proto/hand_landmarker_graph_options.proto',
  package='mediapipe.tasks.vision.hand_landmarker.proto',
  syntax='proto2',
  serialized_options=b'\n6com.google.mediapipe.tasks.vision.handlandmarker.protoB\037HandLandmarkerGraphOptionsProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nSmediapipe/tasks/cc/vision/hand_landmarker/proto/hand_landmarker_graph_options.proto\x12,mediapipe.tasks.vision.hand_landmarker.proto\x1a$mediapipe/framework/calculator.proto\x1a\x30mediapipe/tasks/cc/core/proto/base_options.proto\x1aOmediapipe/tasks/cc/vision/hand_detector/proto/hand_detector_graph_options.proto\x1a[mediapipe/tasks/cc/vision/hand_landmarker/proto/hand_landmarks_detector_graph_options.proto\"\xe5\x03\n\x1aHandLandmarkerGraphOptions\x12=\n\x0c\x62\x61se_options\x18\x01 \x01(\x0b\x32\'.mediapipe.tasks.core.proto.BaseOptions\x12i\n\x1bhand_detector_graph_options\x18\x02 \x01(\x0b\x32\x44.mediapipe.tasks.vision.hand_detector.proto.HandDetectorGraphOptions\x12~\n%hand_landmarks_detector_graph_options\x18\x03 \x01(\x0b\x32O.mediapipe.tasks.vision.hand_landmarker.proto.HandLandmarksDetectorGraphOptions\x12$\n\x17min_tracking_confidence\x18\x04 \x01(\x02:\x03\x30.52w\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xf2\xe2\xd1\xdc\x01 \x01(\x0b\x32H.mediapipe.tasks.vision.hand_landmarker.proto.HandLandmarkerGraphOptionsBY\n6com.google.mediapipe.tasks.vision.handlandmarker.protoB\x1fHandLandmarkerGraphOptionsProto'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_vision_dot_hand__detector_dot_proto_dot_hand__detector__graph__options__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_vision_dot_hand__landmarker_dot_proto_dot_hand__landmarks__detector__graph__options__pb2.DESCRIPTOR,])




_HANDLANDMARKERGRAPHOPTIONS = _descriptor.Descriptor(
  name='HandLandmarkerGraphOptions',
  full_name='mediapipe.tasks.vision.hand_landmarker.proto.HandLandmarkerGraphOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_options', full_name='mediapipe.tasks.vision.hand_landmarker.proto.HandLandmarkerGraphOptions.base_options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hand_detector_graph_options', full_name='mediapipe.tasks.vision.hand_landmarker.proto.HandLandmarkerGraphOptions.hand_detector_graph_options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hand_landmarks_detector_graph_options', full_name='mediapipe.tasks.vision.hand_landmarker.proto.HandLandmarkerGraphOptions.hand_landmarks_detector_graph_options', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_tracking_confidence', full_name='mediapipe.tasks.vision.hand_landmarker.proto.HandLandmarkerGraphOptions.min_tracking_confidence', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.5),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.tasks.vision.hand_landmarker.proto.HandLandmarkerGraphOptions.ext', index=0,
      number=462713202, type=11, cpp_type=10, label=1,
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
  serialized_start=396,
  serialized_end=881,
)

_HANDLANDMARKERGRAPHOPTIONS.fields_by_name['base_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2._BASEOPTIONS
_HANDLANDMARKERGRAPHOPTIONS.fields_by_name['hand_detector_graph_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_vision_dot_hand__detector_dot_proto_dot_hand__detector__graph__options__pb2._HANDDETECTORGRAPHOPTIONS
_HANDLANDMARKERGRAPHOPTIONS.fields_by_name['hand_landmarks_detector_graph_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_vision_dot_hand__landmarker_dot_proto_dot_hand__landmarks__detector__graph__options__pb2._HANDLANDMARKSDETECTORGRAPHOPTIONS
DESCRIPTOR.message_types_by_name['HandLandmarkerGraphOptions'] = _HANDLANDMARKERGRAPHOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HandLandmarkerGraphOptions = _reflection.GeneratedProtocolMessageType('HandLandmarkerGraphOptions', (_message.Message,), {
  'DESCRIPTOR' : _HANDLANDMARKERGRAPHOPTIONS,
  '__module__' : 'mediapipe.tasks.cc.vision.hand_landmarker.proto.hand_landmarker_graph_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.vision.hand_landmarker.proto.HandLandmarkerGraphOptions)
  })
_sym_db.RegisterMessage(HandLandmarkerGraphOptions)

_HANDLANDMARKERGRAPHOPTIONS.extensions_by_name['ext'].message_type = _HANDLANDMARKERGRAPHOPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_HANDLANDMARKERGRAPHOPTIONS.extensions_by_name['ext'])

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
