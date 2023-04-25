FROM golang:1.20 as build-stage

RUN apt-get update && apt-get -y install git

RUN git clone https://github.com/docker-hy/material-applications.git

ENV REQUEST_ORIGIN=http://localhost:5000

RUN cd /go/material-applications/example-backend && CGO_ENABLED=0 go build

FROM scratch

COPY --from=build-stage /go/material-applications/example-backend/server .

CMD ["/server"]