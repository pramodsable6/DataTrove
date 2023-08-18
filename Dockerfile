FROM continuumio/miniconda3
LABEL Author='Pramod Vijay Sable'
LABEL version="1.0"

RUN apt-get update

RUN apt-get install -y default-jdk
COPY environment.yml .
RUN conda env create -f environment.yml
