from mongoengine import connect
from app import app

connect('selling-service')
app.run(host='0.0.0.0')