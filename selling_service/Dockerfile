FROM python:3-alpine

WORKDIR /app

ADD . /app

RUN apk add --update gcc libc-dev linux-headers && rm -rf /var/cache/apk/*

RUN pip install -r requirements.txt

EXPOSE 5000

ENV NAME selling-service

CMD ["python", "run.py"]