FROM python:3.9.4

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y sudo && apt-get install -y vim && apt-get upgrade -y

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip -r /requirements.txt

RUN mkdir promo
WORKDIR /promo
COPY ./promo /promo

RUN adduser --disabled-password --gecos '' python
RUN adduser python sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER python
