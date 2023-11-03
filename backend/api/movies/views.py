from flask_restx import Namespace, Resource, fields, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from http import HTTPStatus
from ..models.users import User
from flask_jwt_extended import jwt_required

# Define a namespace for the users
users_namespace = Namespace("users", "User management")

# Define a model for user data
user_model = users_namespace.model('User', {
    'id': fields.Integer(readonly=True, description='User ID'),
    'username': fields.String(required=True, description='Username'),
    'email': fields.String(required=True, description='Email'),
    'password_hash': fields.String(description='Password Hash'),
    'created_at': fields.DateTime(description='User creation timestamp'),
    'updated_at': fields.DateTime(description='User last update timestamp'),
})


