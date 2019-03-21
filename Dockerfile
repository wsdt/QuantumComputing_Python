FROM continuumio/miniconda3

# (c) Riedl A. Kevin, 2019
# https://github.com/wsdt
# https://www.linkedin.com/in/kevin-riedl-947219158
MAINTAINER Riedl A. Kevin
ARG BASE_PATH=./qapp

RUN conda install -c rigetti pyquil

# Copy source files into image
COPY ./src $BASE_PATH/src
COPY ./conf $BASE_PATH/conf
ENV PATH=$PATH:$BASE_PATH
ENV PYTHONPATH $BASE_PATH

# Execute main-file
CMD python /qapp/src/qbit_love.py