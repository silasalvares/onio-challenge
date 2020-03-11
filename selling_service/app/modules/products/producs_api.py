import pika
from flask import Blueprint

from app.utils.rest import JsonResponse, validate_schema
from app.modules.products import products_service
from app.modules.products.products_schemas import NewProductSchema, ProductSchema

products = Blueprint('products', __name__, url_prefix='/products')

@products.route('/', methods=['POST'])
@validate_schema(NewProductSchema())
def create_product(schema_data):
    new_product = products_service.create_product(schema_data)
    return JsonResponse(data=ProductSchema().dump(new_product)).jsonify()
    
# class Products(Resource):

#     def get(self):
#         # products_service.create_product({
#         #     'name': 'Name 1',
#         #     'description': 'Teste',
#         #     'price': 10.0
#         # })
#         # credentials = pika.PlainCredentials('guest', 'guest')
#         # parameters = pika.ConnectionParameters(
#         #     host='172.20.0.2')
#         # connection = pika.BlockingConnection(parameters)
#         # print(connection.is_open)
#         # channel = connection.channel()
#         # channel.queue_declare('test')
#         # if channel.basic_publish(
#         #         exchange='',
#         #         routing_key='test',
#         #         body='Hello World 2!',
#         #     ):
#         #     print('OK')
#         # else:
#         #     print('ERRO')
#         #     connection.close()
#         #     print('Create')
#         return {'hello': 'world'} 