# Create the Stubs

Build the server and client stubs from the proto files:

    $ python -m grpc.tools.protoc -I../skl --python_out=. --grpc_python_out=. ../skl/skl.proto

# SKL Service

Build the skl-server Docker image:

    $ docker build -f skl-server/Dockerfile \
      -t pprett/skl-server:0.0.1 \
      skl-server/

Upload the skl-server image to a Docker registry:

    $ docker push pprett/skl-server:0.0.1