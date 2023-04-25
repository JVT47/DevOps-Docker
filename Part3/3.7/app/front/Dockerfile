FROM node:16.20-alpine3.16

RUN apk add --no-cache git 
RUN    npm install -g serve 
RUN    git clone https://github.com/docker-hy/material-applications.git 
RUN    cd /material-applications/example-frontend/ && npm install 
RUN    cd /material-applications/example-frontend/ && npm run build 
RUN    adduser -S appuser

ENV REACT_APP_BACKEND_URL=http://localhost:8080

USER appuser

CMD cd /material-applications/example-frontend/ && serve -s -l 5000 build
