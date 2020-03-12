from flask import Flask
from flask_restx import Api
from mongoengine import connect

app = Flask(__name__)
api = Api(app)

from app.modules.products.producs_api import products as products_module
app.register_blueprint(products_module)
products_module_api = Api(products_module, doc='/doc/')
# from app.modules.clients.clients_api import clients as clients_module
# app.register_blueprint(clients_module)
# from app.modules.selling.selling_api import selling as selling_module
# app.register_blueprint(selling_module)