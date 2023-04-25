FROM node:16.20.0

RUN apt-get update -y && apt-get install git -y && \
    npm install -g serve && \
    git clone https://github.com/docker-hy/material-applications.git && \
    cd /material-applications/example-frontend/ && npm install && \
    cd /material-applications/example-frontend/ && npm run build && \
    useradd -m appuser

ENV REACT_APP_BACKEND_URL=http://localhost:8080

USER appuser

CMD cd /material-applications/example-frontend/ && serve -s -l 5000 build
