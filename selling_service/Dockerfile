FROM python:3-alpine

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV NAME selling-service

CMD ["python", "run.py"]