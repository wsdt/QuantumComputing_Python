FROM continuumio/miniconda3

RUN conda install -c rigetti pyquil

COPY ./src ./src

CMD python ./src/qbit_love.py