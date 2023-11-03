from flask import request
from flask_restx import Namespace, Resource, fields
from werkzeug.security import generate_password_hash, check_password_hash
from  ..models.users import User
from http import HTTPStatus

# jwt imports
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


auth_namespace=Namespace("auth", "handle user authentication")
signUp_model = auth_namespace.model(
    'SignUp', {
        'username': fields.String(description="Username", required=True),
        'email': fields.String(description="Email", required=True),
        'password': fields.String(description="Password", required=True),
    }
)

user_model = auth_namespace.model(
    'User', {
        'username': fields.String(description="Username"),
        'email': fields.String(description="Email"),
        'created_at': fields.DateTime(description="Date when user was created")
    }
)

login_model = auth_namespace.model(
    'Login', {
        "username": fields.String(description="Username", required=True),
        "password": fields.String(description="Password", required=True)
    }
)
@auth_namespace.route("/signUp")
class UserAuth(Resource):
    @auth_namespace.expect(signUp_model)
    @auth_namespace.marshal_with(user_model)
    def post(self):
        """create new user"""
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if User.query.filter_by(username=username).first():
            return {
                "error": "User already exists"
            }, HTTPStatus.BAD_REQUEST

        user = User(username=username, email=email, password=generate_password_hash(password))
        user.save()
        return user, HTTPStatus.OK
    
@auth_namespace.route("/users")
class GetUsers(Resource):
    @auth_namespace.marshal_with(user_model, as_list=True)
    @jwt_required()
    def get(self):
        """List all registered users"""
        
        users = User.query.all()
        return users, HTTPStatus.OK

  
@auth_namespace.route('/user/<int:id>')
class User_by_id(Resource):
    @auth_namespace.marshal_with(user_model)
    @jwt_required()
    def get(self, id):
        """retrieve user by id"""
        user = User.query.get(id)
        if not user:
            return {'message': 'User not found'}, HTTPStatus.NOT_FOUND
        return user, HTTPStatus.OK

 
    @jwt_required()
    def delete(self, id):
        """delete user by id"""
        user = User.query.get(id)
        if not user:
            return {'message': 'User not found'}, HTTPStatus.NOT_FOUND
        user.delete()
        return {'message': 'User deleted'}, HTTPStatus.OK


@auth_namespace.route("/login")
class Login(Resource):
    @auth_namespace.expect(login_model)
    def post(self):
        """generate token based on authenticated user"""
        data = request.get_json()
        user = User.query.filter_by(username=data.get("username")).first()

        if user is not None and check_password_hash(user.password, data.get("password")):
            access_token = create_access_token(identity=user.username)
            refresh_token = create_refresh_token(identity=user.username)

            response = {
                "access_token": access_token,
                "refresh_token": refresh_token
            }

            return response, HTTPStatus.OK

        return {"error": "User does not exist or invalid credentials"}, HTTPStatus.NOT_FOUND


@auth_namespace.route("/refresh")
class RefreshToken(Resource):
    @jwt_required(refresh=True)
    def post(self):
        username = get_jwt_identity()

        if username:
            access_token = create_access_token(identity=username)

            return {'access_token': access_token}, HTTPStatus.OK

        return {"error": "Token invalid or not passed"}, HTTPStatus.BAD_REQUEST
