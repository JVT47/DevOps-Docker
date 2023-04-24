FROM node:16.18.1

EXPOSE 500

RUN apt-get update && apt-get -y install git

RUN npm install -g serve

RUN git clone https://github.com/docker-hy/material-applications.git

RUN cd /material-applications/example-frontend/ && npm install

RUN cd /material-applications/example-frontend/ && npm run build

CMD cd /material-applications/example-frontend/ && serve -s -l 5000 build

