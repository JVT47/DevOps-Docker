FROM golang:1.20

EXPOSE 8080

RUN apt-get update && apt-get -y install git

RUN git clone https://github.com/docker-hy/material-applications.git

ENV REQUEST_ORIGIN=http://localhost:5000

RUN cd /go/material-applications/example-backend && go build

CMD cd /go/material-applications/example-backend/ && ./server