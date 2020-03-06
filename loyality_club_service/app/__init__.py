from flask import Flask 
from flask_restx import Api

app = Flask(__name__)
api = Api(app)

@app.route('/event')
def receive_event():
    print('Event Received!')
    return ''