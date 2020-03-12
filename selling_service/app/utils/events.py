import pika

def emit_user_loyality_credit():
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters(host='localhost', credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare('test')
    if channel.basic_publish(
            exchange='',
            routing_key='test',
            body='Hello World 8!',
        ):
        print('OK')
    else:
        print('ERRO')

    connection.close()
    # return {'hello': 'world'} 


