from flask import Flask 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app.modules.loyality.loyality_api import loyality as loyality_module
app.register_blueprint(loyality_module)