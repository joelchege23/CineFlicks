from flask import Flask
from .auth.views import  auth_namespace
from flask_restx import Api
from .config.config import config_dict

def create_app():
    app=Flask(__name__)
    app.config.from_object(config_dict['dev'])
    api=Api(app)

    # add our api blueprints

    api.add_namespace(auth_namespace)

    return app