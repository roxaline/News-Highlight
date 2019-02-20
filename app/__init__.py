from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig

app = Flask(__name__,instance_relative_config = True)
bootstrap = Bootstrap(app)

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views

