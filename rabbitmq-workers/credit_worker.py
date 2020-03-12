import pika
import requests

def on_message(channel, method_frame, header_frame, body):
    message = {'delivery_tag': method_frame.delivery_tag,
        'message': body}
    
    try:
        res = requests.get('http://localhost:5001/')
        print(res)
        #print(str(message['message']))
        pass
    except (Exception):
        print('Erro')

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(
    host='localhost', credentials=credentials)    
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.basic_consume(queue='test', on_message_callback=on_message)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()
