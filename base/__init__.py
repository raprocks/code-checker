from flask import Flask

app = Flask(__name__)
app.config['DEBUG']=True
app.config['SECRET_KEY'] = '43b5c2f118b55bb933fd579455e66247'

from base import routes
