FROM python:3-alpine

WORKDIR /app

ADD . /app

RUN apk add --no-cache git

RUN pip install -r requirements.txt

EXPOSE 5000

ENV NAME loyality-service

CMD ["python", "run.py"]