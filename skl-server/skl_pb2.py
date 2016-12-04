# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: skl.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import predict_pb2 as predict__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='skl.proto',
  package='skl',
  syntax='proto3',
  serialized_pb=_b('\n\tskl.proto\x12\x03skl\x1a\rpredict.proto2O\n\x11PredictionService\x12:\n\x07Predict\x12\x16.skl.PredictionRequest\x1a\x17.skl.PredictionResponseB\x03\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[predict__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\370\001\001'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class PredictionServiceStub(object):
  """The Skl service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Predict = channel.unary_unary(
        '/skl.PredictionService/Predict',
        request_serializer=predict__pb2.PredictionRequest.SerializeToString,
        response_deserializer=predict__pb2.PredictionResponse.FromString,
        )


class PredictionServiceServicer(object):
  """The Skl service definition.
  """

  def Predict(self, request, context):
    """Returns a prediction
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PredictionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Predict': grpc.unary_unary_rpc_method_handler(
          servicer.Predict,
          request_deserializer=predict__pb2.PredictionRequest.FromString,
          response_serializer=predict__pb2.PredictionResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'skl.PredictionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaPredictionServiceServicer(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  """The Skl service definition.
  """
  def Predict(self, request, context):
    """Returns a prediction
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaPredictionServiceStub(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  """The Skl service definition.
  """
  def Predict(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Returns a prediction
    """
    raise NotImplementedError()
  Predict.future = None


def beta_create_PredictionService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_deserializers = {
    ('skl.PredictionService', 'Predict'): predict__pb2.PredictionRequest.FromString,
  }
  response_serializers = {
    ('skl.PredictionService', 'Predict'): predict__pb2.PredictionResponse.SerializeToString,
  }
  method_implementations = {
    ('skl.PredictionService', 'Predict'): face_utilities.unary_unary_inline(servicer.Predict),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_PredictionService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_serializers = {
    ('skl.PredictionService', 'Predict'): predict__pb2.PredictionRequest.SerializeToString,
  }
  response_deserializers = {
    ('skl.PredictionService', 'Predict'): predict__pb2.PredictionResponse.FromString,
  }
  cardinalities = {
    'Predict': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'skl.PredictionService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
