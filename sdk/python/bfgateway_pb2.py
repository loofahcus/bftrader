# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bfgateway.proto

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
  name='bfgateway.proto',
  package='bftrader.bfgateway',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x62\x66gateway.proto\x12\x12\x62\x66trader.bfgateway\x1a\x0e\x62\x66trader.proto2\x90\x05\n\x10\x42\x66GatewayService\x12<\n\x07\x43onnect\x12\x16.bftrader.BfConnectReq\x1a\x17.bftrader.BfConnectResp\"\x00\x12/\n\x05SetKv\x12\x12.bftrader.BfKvData\x1a\x10.bftrader.BfVoid\"\x00\x12\x31\n\x05GetKv\x12\x12.bftrader.BfKvData\x1a\x12.bftrader.BfKvData\"\x00\x12\x45\n\x0bGetContract\x12\x1a.bftrader.BfGetContractReq\x1a\x18.bftrader.BfContractData\"\x00\x12\x41\n\x0fGetContractList\x12\x10.bftrader.BfVoid\x1a\x18.bftrader.BfContractData\"\x00\x30\x01\x12\x39\n\tSubscribe\x12\x18.bftrader.BfSubscribeReq\x1a\x10.bftrader.BfVoid\"\x00\x12:\n\tSendOrder\x12\x14.bftrader.BfOrderReq\x1a\x15.bftrader.BfOrderResp\"\x00\x12=\n\x0b\x43\x61ncelOrder\x12\x1a.bftrader.BfCancelOrderReq\x1a\x10.bftrader.BfVoid\"\x00\x12\x34\n\x0cQueryAccount\x12\x10.bftrader.BfVoid\x1a\x10.bftrader.BfVoid\"\x00\x12\x35\n\rQueryPosition\x12\x10.bftrader.BfVoid\x1a\x10.bftrader.BfVoid\"\x00\x12-\n\x05\x43lose\x12\x10.bftrader.BfVoid\x1a\x10.bftrader.BfVoid\"\x00\x42\x03\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[bftrader__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\370\001\001'))
import abc
from grpc.beta import implementations as beta_implementations
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

class BetaBfGatewayServiceServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Connect(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def SetKv(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetKv(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetContract(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetContractList(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def Subscribe(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def SendOrder(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def CancelOrder(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def QueryAccount(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def QueryPosition(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def Close(self, request, context):
    raise NotImplementedError()

class BetaBfGatewayServiceStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Connect(self, request, timeout):
    raise NotImplementedError()
  Connect.future = None
  @abc.abstractmethod
  def SetKv(self, request, timeout):
    raise NotImplementedError()
  SetKv.future = None
  @abc.abstractmethod
  def GetKv(self, request, timeout):
    raise NotImplementedError()
  GetKv.future = None
  @abc.abstractmethod
  def GetContract(self, request, timeout):
    raise NotImplementedError()
  GetContract.future = None
  @abc.abstractmethod
  def GetContractList(self, request, timeout):
    raise NotImplementedError()
  @abc.abstractmethod
  def Subscribe(self, request, timeout):
    raise NotImplementedError()
  Subscribe.future = None
  @abc.abstractmethod
  def SendOrder(self, request, timeout):
    raise NotImplementedError()
  SendOrder.future = None
  @abc.abstractmethod
  def CancelOrder(self, request, timeout):
    raise NotImplementedError()
  CancelOrder.future = None
  @abc.abstractmethod
  def QueryAccount(self, request, timeout):
    raise NotImplementedError()
  QueryAccount.future = None
  @abc.abstractmethod
  def QueryPosition(self, request, timeout):
    raise NotImplementedError()
  QueryPosition.future = None
  @abc.abstractmethod
  def Close(self, request, timeout):
    raise NotImplementedError()
  Close.future = None

def beta_create_BfGatewayService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
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
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  request_deserializers = {
    ('bftrader.bfgateway.BfGatewayService', 'CancelOrder'): bftrader_pb2.BfCancelOrderReq.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'Close'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'Connect'): bftrader_pb2.BfConnectReq.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'GetContract'): bftrader_pb2.BfGetContractReq.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'GetContractList'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'GetKv'): bftrader_pb2.BfKvData.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'QueryAccount'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'QueryPosition'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'SendOrder'): bftrader_pb2.BfOrderReq.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'SetKv'): bftrader_pb2.BfKvData.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'Subscribe'): bftrader_pb2.BfSubscribeReq.FromString,
  }
  response_serializers = {
    ('bftrader.bfgateway.BfGatewayService', 'CancelOrder'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'Close'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'Connect'): bftrader_pb2.BfConnectResp.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'GetContract'): bftrader_pb2.BfContractData.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'GetContractList'): bftrader_pb2.BfContractData.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'GetKv'): bftrader_pb2.BfKvData.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'QueryAccount'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'QueryPosition'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'SendOrder'): bftrader_pb2.BfOrderResp.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'SetKv'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'Subscribe'): bftrader_pb2.BfVoid.SerializeToString,
  }
  method_implementations = {
    ('bftrader.bfgateway.BfGatewayService', 'CancelOrder'): face_utilities.unary_unary_inline(servicer.CancelOrder),
    ('bftrader.bfgateway.BfGatewayService', 'Close'): face_utilities.unary_unary_inline(servicer.Close),
    ('bftrader.bfgateway.BfGatewayService', 'Connect'): face_utilities.unary_unary_inline(servicer.Connect),
    ('bftrader.bfgateway.BfGatewayService', 'GetContract'): face_utilities.unary_unary_inline(servicer.GetContract),
    ('bftrader.bfgateway.BfGatewayService', 'GetContractList'): face_utilities.unary_stream_inline(servicer.GetContractList),
    ('bftrader.bfgateway.BfGatewayService', 'GetKv'): face_utilities.unary_unary_inline(servicer.GetKv),
    ('bftrader.bfgateway.BfGatewayService', 'QueryAccount'): face_utilities.unary_unary_inline(servicer.QueryAccount),
    ('bftrader.bfgateway.BfGatewayService', 'QueryPosition'): face_utilities.unary_unary_inline(servicer.QueryPosition),
    ('bftrader.bfgateway.BfGatewayService', 'SendOrder'): face_utilities.unary_unary_inline(servicer.SendOrder),
    ('bftrader.bfgateway.BfGatewayService', 'SetKv'): face_utilities.unary_unary_inline(servicer.SetKv),
    ('bftrader.bfgateway.BfGatewayService', 'Subscribe'): face_utilities.unary_unary_inline(servicer.Subscribe),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_BfGatewayService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
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
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  request_serializers = {
    ('bftrader.bfgateway.BfGatewayService', 'CancelOrder'): bftrader_pb2.BfCancelOrderReq.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'Close'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'Connect'): bftrader_pb2.BfConnectReq.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'GetContract'): bftrader_pb2.BfGetContractReq.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'GetContractList'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'GetKv'): bftrader_pb2.BfKvData.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'QueryAccount'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'QueryPosition'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'SendOrder'): bftrader_pb2.BfOrderReq.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'SetKv'): bftrader_pb2.BfKvData.SerializeToString,
    ('bftrader.bfgateway.BfGatewayService', 'Subscribe'): bftrader_pb2.BfSubscribeReq.SerializeToString,
  }
  response_deserializers = {
    ('bftrader.bfgateway.BfGatewayService', 'CancelOrder'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'Close'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'Connect'): bftrader_pb2.BfConnectResp.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'GetContract'): bftrader_pb2.BfContractData.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'GetContractList'): bftrader_pb2.BfContractData.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'GetKv'): bftrader_pb2.BfKvData.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'QueryAccount'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'QueryPosition'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'SendOrder'): bftrader_pb2.BfOrderResp.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'SetKv'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfgateway.BfGatewayService', 'Subscribe'): bftrader_pb2.BfVoid.FromString,
  }
  cardinalities = {
    'CancelOrder': cardinality.Cardinality.UNARY_UNARY,
    'Close': cardinality.Cardinality.UNARY_UNARY,
    'Connect': cardinality.Cardinality.UNARY_UNARY,
    'GetContract': cardinality.Cardinality.UNARY_UNARY,
    'GetContractList': cardinality.Cardinality.UNARY_STREAM,
    'GetKv': cardinality.Cardinality.UNARY_UNARY,
    'QueryAccount': cardinality.Cardinality.UNARY_UNARY,
    'QueryPosition': cardinality.Cardinality.UNARY_UNARY,
    'SendOrder': cardinality.Cardinality.UNARY_UNARY,
    'SetKv': cardinality.Cardinality.UNARY_UNARY,
    'Subscribe': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'bftrader.bfgateway.BfGatewayService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
