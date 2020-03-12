from mongoengine import connect
from app import app

connect('selling-service', host='mongo-server')
app.run(host='0.0.0.0')