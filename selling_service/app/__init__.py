from flask import Flask
from flask_restx import Api

app = Flask(__name__)
webapi = Api(app)

from app.modules.products.producs_api import Products
webapi.add_resource(Products, '/products')



