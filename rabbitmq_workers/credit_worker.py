import time
import pika
import requests

def on_message(channel, method_frame, header_frame, body):
    message = {'delivery_tag': method_frame.delivery_tag,
        'message': body}
    
    try:
        res = requests.get('http://loyality-service:5001/')
        print(res)
        #print(str(message['message']))
        pass
    except (Exception):
        print('Erro')

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(
    host='rabbitmq-server', credentials=credentials)    

connection = None

try:
    connection = pika.BlockingConnection(parameters)
except:
    connection  = None

while not connection:
    print('Trying RabbitMQ connection...')
    time.sleep(10)
    try:
        connection = pika.BlockingConnection(parameters)
    except:
        connection = None

channel = connection.channel()
channel.queue_declare('credits')
channel.basic_consume(queue='credits', on_message_callback=on_message)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()
