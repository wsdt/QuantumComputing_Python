FROM continuumio/miniconda3

# (c) Riedl A. Kevin, 2019
# https://github.com/wsdt
# https://www.linkedin.com/in/kevin-riedl-947219158
MAINTAINER Riedl A. Kevin

RUN conda install -c rigetti pyquil

# Copy source files into image
COPY ./src ./src

# Execute main-file
CMD python ./src/qbit_love.py