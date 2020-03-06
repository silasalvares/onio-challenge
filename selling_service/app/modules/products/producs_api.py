from flask_restx import Resource
from .products_service import ProductsService

class Products(Resource):

    def get(self):
        ProductsService().create_product()
        return {'hello': 'world'}