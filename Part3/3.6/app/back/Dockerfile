FROM golang:1.20

RUN apt-get update && apt-get -y install git && \
    git clone https://github.com/docker-hy/material-applications.git && \
    cd /go/material-applications/example-backend && go build && \
    useradd -m appuser

ENV REQUEST_ORIGIN=http://localhost:5000

USER appuser

CMD cd /go/material-applications/example-backend/ && ./server