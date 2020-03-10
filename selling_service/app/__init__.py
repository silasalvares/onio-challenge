from flask import Flask
from flask_restx import Api
from mongoengine import connect

app = Flask(__name__)
webapi = Api(app)

db = connect('selling-microservice')

from app.modules.products.producs_api import Products
webapi.add_resource(Products, '/products')



