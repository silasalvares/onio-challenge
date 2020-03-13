import pika

def emit_user_loyality_credit(selling):
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters(host='rabbitmq-server', credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    
    channel = connection.channel()
    channel.queue_declare(queue='credits')
    if channel.basic_publish(
            exchange='',
            routing_key='credits',
            body={'cpf': selling.client.cpf, 'value': selling.value},
        ):
        print('OK')
    else:
        print('ERRO')

    connection.close()


