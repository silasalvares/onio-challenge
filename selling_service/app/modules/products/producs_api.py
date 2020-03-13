import pika
from flask import Blueprint
from flask_restx import Resource

from app.utils.rest import JsonResponse, validate_schema
from app.modules.products import products_service
from app.modules.products.products_schemas import NewProductSchema, ProductSchema

products = Blueprint('products', __name__, url_prefix='/products')

products = Blueprint('products', __name__, url_prefix='/products')

@products.route('/', methods=['POST'])
@validate_schema(NewProductSchema())
def create_product(schema_data):
    new_product = products_service.create_product(schema_data)
    return JsonResponse(data=ProductSchema().dump(new_product)).jsonify()