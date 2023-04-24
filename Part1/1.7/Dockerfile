FROM ubuntu:20.04

WORKDIR /usr/src/app

COPY script.sh .

RUN apt-get update
RUN apt-get -y install curl

CMD ./script.sh