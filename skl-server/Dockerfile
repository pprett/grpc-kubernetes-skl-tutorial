FROM ubuntu:14.04
MAINTAINER Peter Prettenhofer <peter.prettenhofer@gmail.com>

# System packages 
RUN apt-get update && apt-get install -y curl

# Install miniconda to /miniconda
RUN curl -LO http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
RUN bash Miniconda-latest-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda-latest-Linux-x86_64.sh
ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda

# Python packages from conda
RUN conda install -y \
    enum34==1.1.6 \
    futures==3.0.5 \
    scikit-learn==0.18.1

RUN pip install \
    protobuf==3.1.0.post1 \
    grpcio==1.0.1 \
    grpcio-tools==1.0.1

COPY skl-server skl-server
ENTRYPOINT ["python", "/skl-server/skl_server.py"]