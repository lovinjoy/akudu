# Test tcp way connect kudu
import socket
import time

from akudu.kudu.rpc.rpc_header_pb2 import RequestHeader
from akudu.kudu.rpc.rpc_header_pb2 import ResponseHeader
from akudu.kudu.rpc.rpc_header_pb2 import NegotiatePB
from akudu.kudu.rpc.rpc_header_pb2 import ErrorStatusPB
from akudu.kudu.rpc.rpc_header_pb2 import AuthenticationTypePB
from akudu.kudu.rpc.rpc_header_pb2 import ConnectionContextPB

from akudu.kudu.rpc.rpc_header_pb2 import RemoteMethodPB
from akudu.kudu.master.master_pb2 import ListTablesRequestPB
from akudu.kudu.master.master_pb2 import ListTablesResponsePB

from akudu.kudu.server.server_base_pb2 import GetStatusRequestPB
from akudu.kudu.server.server_base_pb2 import GetStatusResponsePB

from test import input_stream
from test import output_stream

def call_req(header_pb, body_pb):
    buf = b''

    header = header_pb.SerializeToString()
    header_o = output_stream.OutputStream()
    header_o.AppendVarint32(header_pb.ByteSize())
    header = header_o.ToString() + header

    body = body_pb.SerializeToString()
    body_o = output_stream.OutputStream()
    body_o.AppendVarint32(body_pb.ByteSize())
    body = body_o.ToString() + body

    total_byte_size = len(header + body)
    buf = total_byte_size.to_bytes(4, 'big') + header + body
    print('Request:', header, body)
    return buf


def extra_resp(resp_bytes, body_pb=NegotiatePB):
    message_size = int.from_bytes(resp_bytes[:4], 'big')

    header_i = input_stream.InputStreamArray(resp_bytes[4:])
    header_size = header_i.ReadVarint32()
    header_data_start_pos = 4 + header_i.Position()

    body_i = input_stream.InputStreamArray(resp_bytes[header_data_start_pos + header_size:])
    body_size = body_i.ReadVarint32()
    body_data_start_pos = header_data_start_pos + header_size + body_i.Position()
    body = resp_bytes[body_data_start_pos: body_data_start_pos+body_size]

    resp_head = ResponseHeader.FromString(resp_bytes[header_data_start_pos: header_data_start_pos+header_size])

    print('--------- Resp Header ----------')
    print(resp_head)

    if resp_head.is_error:
        resp_body = ErrorStatusPB.FromString(body)
    else:
        resp_body = body_pb.FromString(body)

    print('---------- Resp Body -----------')
    print(resp_body)



host = '192.168.50.112'
port = 7051
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cr = s.connect((host, port))

print('Connected... ', cr)

s.sendall(b'hrpc\x09\x00\x00')
print(r"Sent HRPC: b'hrpc\x09\x00\x00'")
time.sleep(0.1)

# Step 1
header_pb = RequestHeader(call_id=-33)
body_pb = NegotiatePB(
        step=1,
        authn_types=[AuthenticationTypePB(sasl={})],
        sasl_mechanisms=[NegotiatePB.SaslMechanism(mechanism='PLAIN')],
        token=b'kudu'
        )
s.sendall(call_req(header_pb, body_pb))

time.sleep(1)
data = s.recv(2048)
print('Received', data)
extra_resp(data)


# Step 2
header_pb = RequestHeader(call_id=-33)
body_pb = NegotiatePB(
        step=2,
        authn_types=[AuthenticationTypePB(sasl={})],
        sasl_mechanisms=[NegotiatePB.SaslMechanism(mechanism='PLAIN')],
        token=b'\x00kudu\x00')
s.sendall(call_req(header_pb, body_pb))

time.sleep(1)
data = s.recv(2048)
print('Received', data)
extra_resp(data)


# Step 3
header_pb = RequestHeader(call_id=-3)
body_pb = ConnectionContextPB()
s.sendall(call_req(header_pb, body_pb))
time.sleep(1)
print("Negotiate Finished...")


header_pb = RequestHeader(call_id=0, remote_method=RemoteMethodPB(service_name="kudu.server.GenericService", method_name="GetStatus"))
body_pb = GetStatusRequestPB()
s.sendall(call_req(header_pb, body_pb))

header_pb = RequestHeader(call_id=1, remote_method=RemoteMethodPB(service_name="kudu.master.MasterService", method_name="ListTables"))
body_pb = ListTablesRequestPB()
s.sendall(call_req(header_pb, body_pb))
time.sleep(1)
data = s.recv(65536)
print('Received', data)
extra_resp(data, GetStatusResponsePB)

exit()

# List Tables

header_pb = RequestHeader(call_id=0, remote_method=RemoteMethodPB(service_name="kudu.master.MasterService", method_name="ListTables"))
body_pb = ListTablesRequestPB()
s.sendall(call_req(header_pb, body_pb))
time.sleep(1)
data = s.recv(65536)
print('Received', data)
extra_resp(data, ListTablesResponsePB)

# Scan rq_col.tb_dwd_user_did


# s.sendall( b'\x00\x00\x00\x0f' +
#         b"\x0b" + b'\x18\xdf\xff\xff\xff\xff\xff\xff\xff\xff\x01' +
#         b'\x02' + b'\x10\x02')

# s.sendall(b'\x00\x00\x00\x29' +  b"\x27" + b"\n\x19kudu.master.MasterService\x12\nListTables" + b'\x00')
# print('Sent 1.5')
# for i in range(5):
#     time.sleep(2)
#     data = s.recv(1024)
#     print('Received', repr(data))
# time.sleep(0.1)
# 
# s.sendall(b'\x00\x00\x00\x17' + b'\x09' + b'\x08\x0a\x1a\x03\x41\x64\x64\x20\x01' + b'\x0c' + b'\x08\xd4\x90\x80\x91\x01\x10\xf8\xcf\xc4\xed\x04')
# print('Sent 2')
# time.sleep(1)
# data = s.recv(1024)
# print('Received', repr(data))
# 
# time.sleep(1)

# zagfai@tpad:~/Downloads$ find ./kudu-master/src/ -name "*.proto" | xargs python -m grpc_tools.protoc -I./kudu-master/src --python_out=. --grpc_python_out=grpc
# zagfai@tpad:~/Downloads$ find ./kudu-master/src/ -name "*.proto" | xargs protoc -I=kudu-master/src --python_out=pb
