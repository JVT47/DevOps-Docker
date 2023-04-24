FROM golang:1.16

EXPOSE 8080

RUN apt-get update && apt-get -y install git

RUN git clone https://github.com/docker-hy/material-applications.git

RUN cd /go/material-applications/example-backend && go build

CMD cd /go/material-applications/example-backend/ && ./server