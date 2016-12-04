from concurrent import futures
import time

import grpc

import skl_pb2

from predict_pb2 import PredictionSpec
from predict_pb2 import PredictionResponse



_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class PredictionServiceServicer(skl_pb2.PredictionServiceServicer):
    """Provides methods that implement functionality of prediction service. """

    def __init__(self):
        pass

    def Predict(self, request, context):
        pred_spec = PredictionSpec(n_classes=1,
                                   cache_hit=True,
                                   execution_time=1,
                                   class_names=['response'],
                                   model_id=request.model_spec.model_id)

        outputs = {row_id: 0.5 for row_id in  request.input.index}
        return PredictionResponse(prediction_spec=pred_spec,
                                  outputs=outputs)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    skl_pb2.add_PredictionServiceServicer_to_server(
        PredictionServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
