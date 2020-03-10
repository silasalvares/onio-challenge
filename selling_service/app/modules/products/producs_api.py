import pika
from flask_restx import Resource

from app.modules.products import products_service

class Products(Resource):

    def get(self):
        # products_service.create_product({
        #     'name': 'Name 1',
        #     'description': 'Teste',
        #     'price': 10.0
        # })
        # credentials = pika.PlainCredentials('guest', 'guest')
        # parameters = pika.ConnectionParameters(
        #     host='172.20.0.2')
        # connection = pika.BlockingConnection(parameters)
        # print(connection.is_open)
        # channel = connection.channel()
        # channel.queue_declare('test')
        # if channel.basic_publish(
        #         exchange='',
        #         routing_key='test',
        #         body='Hello World 2!',
        #     ):
        #     print('OK')
        # else:
        #     print('ERRO')
        #     connection.close()
        #     print('Create')
        return {'hello': 'world'} 