FROM golang:1.20.3-alpine3.17

RUN apk add --no-cache git 
RUN    git clone https://github.com/docker-hy/material-applications.git 
RUN    cd /go/material-applications/example-backend && go build 
RUN    adduser -S appuser

ENV REQUEST_ORIGIN=http://localhost:5000

USER appuser

CMD cd /go/material-applications/example-backend/ && ./server