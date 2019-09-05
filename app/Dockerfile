FROM node

WORKDIR /app
COPY package.json .
COPY package-lock.json .

RUN npm install

COPY src .
COPY angular.json .
COPY proxy.conf.json .
COPY tsconfig.json .
COPY tslint.json .

RUN npm run prod

FROM nginx

COPY --from=0 /app/dist /static/
COPY static /static/static
COPY .nginx.server.conf /etc/nginx/conf.d/default.conf
COPY .uwsgi.conf /etc/nginx/uwsgi.conf