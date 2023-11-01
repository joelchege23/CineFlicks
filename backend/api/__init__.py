from flask import Flask
from .auth.views import  auth_namespace
from flask_restx import Api


def create_app():
    app=Flask(__name__)

    api=Api(app)

    # add our api blueprints

    api.add_namespace(auth_namespace)

    return app