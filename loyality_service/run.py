from mongoengine import connect, disconnect
from app import app

connect('loyality-service', host='mongo-server')
app.run(host='0.0.0.0', port=5001)