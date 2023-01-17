FROM node:18.13-slim

WORKDIR /code

COPY package.json /code/package.json

RUN npm install

COPY . /code

CMD [ "npm", "start" ]
