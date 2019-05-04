FROM node

RUN mkdir /angular
WORKDIR /angular
COPY unichallenge_client /angular
RUN npm install
RUN npm run prod

FROM nginx

COPY --from=0 /angular/dist/uknow /files/angular
COPY unichallenge_server/static /files/static
