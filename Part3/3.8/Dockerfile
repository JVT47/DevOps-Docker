FROM node:16.20-alpine3.16 as build-stage

RUN    apk add --no-cache git 
RUN    npm install -g serve 
RUN    git clone https://github.com/docker-hy/material-applications.git 
RUN    cd /material-applications/example-frontend/ && npm install 
RUN    cd /material-applications/example-frontend/ && npm run build


FROM node:16.20-alpine3.16

WORKDIR /usr/src/app

RUN npm install -g serve

COPY --from=build-stage /material-applications/example-frontend/build/ /usr/src/app/build/

ENV REACT_APP_BACKEND_URL=http://localhost:8080

RUN adduser -S appuser
USER appuser

CMD cd /usr/src/app/ && serve -s -l 5000 build