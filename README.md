# WORK-IN-PROGRESS

# Development

Create a virtualenv:

    $ mkvirtualenv grpc

Ensure you have pip version `8` or higher:

    $ pip install -U pip

Install dependencies:

    $ pip install -r requirements.txt


## Create the Stubs

Build the server and client stubs from the proto files:

    $ python -m grpc.tools.protoc -Iskl --python_out=skl-server --grpc_python_out=skl-server skl/skl.proto
    $ python -m grpc.tools.protoc -Iskl --python_out=skl-server --grpc_python_out=skl-server skl/predict.proto
    $ python -m grpc.tools.protoc -Iskl --python_out=skl-server --grpc_python_out=skl-server skl/model.proto
    $ python -m grpc.tools.protoc -Iskl --python_out=skl-server --grpc_python_out=skl-server skl/dataframe.proto


# Testing

Start the server:

    $ cd skl-server
    $ python skl_server.py

Start the client:

    $ cd skl-server
    $ python skl_client.py


# SKL Service

## Build Docker images

Build the skl-server Docker image:

    $ docker build -f skl-server/Dockerfile \
      -t pprett/skl-server:0.0.1 \
      skl-server/

Upload the skl-server image to a Docker registry:

    $ docker push pprett/skl-server:0.0.1