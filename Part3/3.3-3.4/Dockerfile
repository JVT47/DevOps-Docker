FROM alpine:latest

COPY builder.sh builder.sh

RUN apk update

RUN apk add --no-cache --upgrade bash
RUN apk add git
RUN apk add docker

RUN chmod +x ./builder.sh

ENV GIT_REPO ${GIT_REPO}
ENV DOCKER_REPO ${DOCKER_REPO}
ENV DOCKER_USER ${DOCKER_USER}
ENV DOCKER_PASS ${DOCKER_PASS}

ENTRYPOINT ./builder.sh ${GIT_REPO} ${DOCKER_REPO}