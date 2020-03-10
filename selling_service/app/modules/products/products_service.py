import pika

from .products_models import Product

def create_product(product_data):
    return Product(**product_data).save()