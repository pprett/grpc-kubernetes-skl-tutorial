from concurrent import futures
import time

import grpc

import skl_pb2


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class SklServicer(skl_pb2.SklServicer):
    """Provides methods that implement functionality of skl server. """
    
    def __init__(self):
        pass

    def Predict(self, request, context):
        return skl_pb2.Response(prediction=0.5)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    skl_pb2.add_SklServicer_to_server(
        SklServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
