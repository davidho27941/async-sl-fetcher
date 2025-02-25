FROM python:3.12 AS base

RUN apt -y update && \
    apt -y install vim && \
    pip install uv && \
    mkdir /root/async-sl-fetcher

COPY . /root/async-sl-fetcher
WORKDIR /root/async-sl-fetcher
RUN uv pip install --system -r requirements.txt

EXPOSE 8888

ENTRYPOINT ./entrypoint.sh