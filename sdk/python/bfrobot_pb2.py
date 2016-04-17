# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bfrobot.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bftrader_pb2 as bftrader__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bfrobot.proto',
  package='bftrader.bfrobot',
  syntax='proto3',
  serialized_pb=_b('\n\rbfrobot.proto\x12\x10\x62\x66trader.bfrobot\x1a\x0e\x62\x66trader.proto2\xd0\x03\n\x0e\x42\x66RobotService\x12\x38\n\x10OnExchangeOpened\x12\x10.bftrader.BfVoid\x1a\x10.bftrader.BfVoid\"\x00\x12\x32\n\x06OnTick\x12\x14.bftrader.BfTickData\x1a\x10.bftrader.BfVoid\"\x00\x12\x34\n\x07OnError\x12\x15.bftrader.BfErrorData\x1a\x10.bftrader.BfVoid\"\x00\x12\x34\n\x07OnTrade\x12\x15.bftrader.BfTradeData\x1a\x10.bftrader.BfVoid\"\x00\x12\x34\n\x07OnOrder\x12\x15.bftrader.BfOrderData\x1a\x10.bftrader.BfVoid\"\x00\x12:\n\nOnPosition\x12\x18.bftrader.BfPositionData\x1a\x10.bftrader.BfVoid\"\x00\x12\x38\n\tOnAccount\x12\x17.bftrader.BfAccountData\x1a\x10.bftrader.BfVoid\"\x00\x12\x38\n\x10OnExchangeClosed\x12\x10.bftrader.BfVoid\x1a\x10.bftrader.BfVoid\"\x00\x42\x03\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[bftrader__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\370\001\001'))
import abc
from grpc.beta import implementations as beta_implementations
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

class BetaBfRobotServiceServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def OnExchangeOpened(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def OnTick(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def OnError(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def OnTrade(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def OnOrder(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def OnPosition(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def OnAccount(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def OnExchangeClosed(self, request, context):
    raise NotImplementedError()

class BetaBfRobotServiceStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def OnExchangeOpened(self, request, timeout):
    raise NotImplementedError()
  OnExchangeOpened.future = None
  @abc.abstractmethod
  def OnTick(self, request, timeout):
    raise NotImplementedError()
  OnTick.future = None
  @abc.abstractmethod
  def OnError(self, request, timeout):
    raise NotImplementedError()
  OnError.future = None
  @abc.abstractmethod
  def OnTrade(self, request, timeout):
    raise NotImplementedError()
  OnTrade.future = None
  @abc.abstractmethod
  def OnOrder(self, request, timeout):
    raise NotImplementedError()
  OnOrder.future = None
  @abc.abstractmethod
  def OnPosition(self, request, timeout):
    raise NotImplementedError()
  OnPosition.future = None
  @abc.abstractmethod
  def OnAccount(self, request, timeout):
    raise NotImplementedError()
  OnAccount.future = None
  @abc.abstractmethod
  def OnExchangeClosed(self, request, timeout):
    raise NotImplementedError()
  OnExchangeClosed.future = None

def beta_create_BfRobotService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  request_deserializers = {
    ('bftrader.bfrobot.BfRobotService', 'OnAccount'): bftrader_pb2.BfAccountData.FromString,
    ('bftrader.bfrobot.BfRobotService', 'OnError'): bftrader_pb2.BfErrorData.FromString,
    ('bftrader.bfrobot.BfRobotService', 'OnExchangeClosed'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfrobot.BfRobotService', 'OnExchangeOpened'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfrobot.BfRobotService', 'OnOrder'): bftrader_pb2.BfOrderData.FromString,
    ('bftrader.bfrobot.BfRobotService', 'OnPosition'): bftrader_pb2.BfPositionData.FromString,
    ('bftrader.bfrobot.BfRobotService', 'OnTick'): bftrader_pb2.BfTickData.FromString,
    ('bftrader.bfrobot.BfRobotService', 'OnTrade'): bftrader_pb2.BfTradeData.FromString,
  }
  response_serializers = {
    ('bftrader.bfrobot.BfRobotService', 'OnAccount'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfrobot.BfRobotService', 'OnError'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfrobot.BfRobotService', 'OnExchangeClosed'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfrobot.BfRobotService', 'OnExchangeOpened'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfrobot.BfRobotService', 'OnOrder'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfrobot.BfRobotService', 'OnPosition'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfrobot.BfRobotService', 'OnTick'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfrobot.BfRobotService', 'OnTrade'): bftrader_pb2.BfVoid.SerializeToString,
  }
  method_implementations = {
    ('bftrader.bfrobot.BfRobotService', 'OnAccount'): face_utilities.unary_unary_inline(servicer.OnAccount),
    ('bftrader.bfrobot.BfRobotService', 'OnError'): face_utilities.unary_unary_inline(servicer.OnError),
    ('bftrader.bfrobot.BfRobotService', 'OnExchangeClosed'): face_utilities.unary_unary_inline(servicer.OnExchangeClosed),
    ('bftrader.bfrobot.BfRobotService', 'OnExchangeOpened'): face_utilities.unary_unary_inline(servicer.OnExchangeOpened),
    ('bftrader.bfrobot.BfRobotService', 'OnOrder'): face_utilities.unary_unary_inline(servicer.OnOrder),
    ('bftrader.bfrobot.BfRobotService', 'OnPosition'): face_utilities.unary_unary_inline(servicer.OnPosition),
    ('bftrader.bfrobot.BfRobotService', 'OnTick'): face_utilities.unary_unary_inline(servicer.OnTick),
    ('bftrader.bfrobot.BfRobotService', 'OnTrade'): face_utilities.unary_unary_inline(servicer.OnTrade),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_BfRobotService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  request_serializers = {
    ('bftrader.bfrobot.BfRobotService', 'OnAccount'): bftrader_pb2.BfAccountData.SerializeToString,
    ('bftrader.bfrobot.BfRobotService', 'OnError'): bftrader_pb2.BfErrorData.SerializeToString,
    ('bftrader.bfrobot.BfRobotService', 'OnExchangeClosed'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfrobot.BfRobotService', 'OnExchangeOpened'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfrobot.BfRobotService', 'OnOrder'): bftrader_pb2.BfOrderData.SerializeToString,
    ('bftrader.bfrobot.BfRobotService', 'OnPosition'): bftrader_pb2.BfPositionData.SerializeToString,
    ('bftrader.bfrobot.BfRobotService', 'OnTick'): bftrader_pb2.BfTickData.SerializeToString,
    ('bftrader.bfrobot.BfRobotService', 'OnTrade'): bftrader_pb2.BfTradeData.SerializeToString,
  }
  response_deserializers = {
    ('bftrader.bfrobot.BfRobotService', 'OnAccount'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfrobot.BfRobotService', 'OnError'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfrobot.BfRobotService', 'OnExchangeClosed'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfrobot.BfRobotService', 'OnExchangeOpened'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfrobot.BfRobotService', 'OnOrder'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfrobot.BfRobotService', 'OnPosition'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfrobot.BfRobotService', 'OnTick'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfrobot.BfRobotService', 'OnTrade'): bftrader_pb2.BfVoid.FromString,
  }
  cardinalities = {
    'OnAccount': cardinality.Cardinality.UNARY_UNARY,
    'OnError': cardinality.Cardinality.UNARY_UNARY,
    'OnExchangeClosed': cardinality.Cardinality.UNARY_UNARY,
    'OnExchangeOpened': cardinality.Cardinality.UNARY_UNARY,
    'OnOrder': cardinality.Cardinality.UNARY_UNARY,
    'OnPosition': cardinality.Cardinality.UNARY_UNARY,
    'OnTick': cardinality.Cardinality.UNARY_UNARY,
    'OnTrade': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'bftrader.bfrobot.BfRobotService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
