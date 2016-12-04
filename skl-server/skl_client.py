import grpc
import pandas as pd

import skl_pb2
import predict_pb2
import model_pb2

from utils import pandas_to_proto


def run():
    df = pd.DataFrame(columns=list('abc'), data=pd.np.random.rand(10, 3))
    channel = grpc.insecure_channel('localhost:50051')
    stub = skl_pb2.PredictionServiceStub(channel)
    print("-------------- Predict --------------")
    model_spec = model_pb2.ModelSpec(model_id='123abc')
    req = predict_pb2.PredictionRequest(model_spec=model_spec, input=pandas_to_proto(df))
    pred = stub.Predict(req)
    print(pred)


if __name__ == '__main__':
    run()
