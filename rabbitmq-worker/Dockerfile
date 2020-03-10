FROM python:3-alpine

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

ENV NAME worker

CMD ["python", "rabbitmq_worker.py"]