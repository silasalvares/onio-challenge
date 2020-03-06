import pika

class ProductsService():

    def create_product(self):
        credentials = pika.PlainCredentials('guest', 'guest')
        parameters = pika.ConnectionParameters(host='localhost', credentials=credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare('test')
        if channel.basic_publish(
            exchange='',
            routing_key='test',
            body='Hello World 2!',
        ):
            print('OK')
        else:
            print('ERRO')

        connection.close()
        print('Create')    