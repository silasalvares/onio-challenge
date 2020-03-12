FROM python:3-alpine

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

ENV NAME rabbitmq-workers

CMD ["python", "credit_worker.py"]