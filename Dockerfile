# Usage
# docker build -t johnsa1/dffml_operations_github .
# docker run --rm -ti -p 80:8080 johnsa1/dffml_operations_github  -insecure -log debug
#
# curl -v http://127.0.0.1:80/list/sources
FROM ubuntu:20.04

RUN apt-get update && \
  apt-get install -y \
    gcc \
    python3-dev \
    python3-pip \
    python3 \
    ca-certificates && \
  python3 -m pip install -U pip && \
  python3 -m pip install dffml-service-http && \
  apt-get purge -y \
    gcc \
    python3-dev && \
  rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN python3 -m pip install -e .

ENTRYPOINT ["python3", "-m", "dffml", "service", "http", "server", "-addr", "0.0.0.0"]
CMD ["-mc-config", "dffml_operations_github/deploy"]
