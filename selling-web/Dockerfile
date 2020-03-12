FROM node

WORKDIR /app

ADD . /app

RUN npm i

EXPOSE 4200

ENV NAME selling-web

CMD ["npx", "ng", "serve", "--host", "0.0.0.0"]

# CMD ["python", "run.py"]
# COPY /dist/aston-villa-app /usr/share/nginx/html