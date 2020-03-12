from flask import Flask 

app = Flask(__name__)

from app.modules.loyality.loyality_api import loyality as loyality_module
app.register_blueprint(loyality_module)