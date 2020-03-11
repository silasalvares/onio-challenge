import pika
import requests

def on_message(channel, method_frame, header_frame, body):
    message = {'delivery_tag': method_frame.delivery_tag,
        'message': body}

    try:
        print(message)
        res = requests.get('http://localhost:5001/event')
        print(res)
    except (Exception):
        print('Erro')

parameters = pika.ConnectionParameters(
    host='172.20.0.2')    
connection = pika.BlockingConnection(parameters)
print(connection.is_open)
channel = connection.channel()
channel.queue_declare('test')
channel.basic_consume(queue='test', on_message_callback=on_message)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()