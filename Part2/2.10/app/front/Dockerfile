FROM node:16.20.0

RUN apt-get update -y && apt-get install git -y

RUN npm install -g serve

RUN git clone https://github.com/docker-hy/material-applications.git

RUN cd /material-applications/example-frontend/ && npm install

ENV REACT_APP_BACKEND_URL=http://localhost:8080

RUN cd /material-applications/example-frontend/ && npm run build


CMD cd /material-applications/example-frontend/ && serve -s -l 5000 build
