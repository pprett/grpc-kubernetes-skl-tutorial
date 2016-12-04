import grpc

import skl_pb2


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = skl_pb2.SklStub(channel)
    print("-------------- Predict --------------")
    req = skl_pb2.Request(modelid='123abc')
    pred = stub.Predict(req)
    print(pred)


if __name__ == '__main__':
    run()
