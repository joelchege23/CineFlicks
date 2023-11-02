from flask_restx import Namespace, Resource, fields
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from  ..models.users import User
from http import HTTPStatus

# jwt imports
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

auth_namespace=Namespace("auth", "handle user authentication")

signUp_model=auth_namespace.model(
    'User',{
        'user_id':fields.Integer(description="user id"),
        'username':fields.String(description="user name" ,required=True),
        'email':fields.String(description="user email" , required=True),
        'password':fields.String(description="user password" ,required=True),
    }
)

user_model=auth_namespace.model(
    'User',{
        'user_id':fields.Integer(description="user id" ,),
        'username':fields.String(description="user name" ,),
        'email':fields.String(description="user email" ,),
        'created_at':fields.DateTime(description="date when user was created")
    }
)

login_model=auth_namespace.model(
    'User',{
        "username":fields.String(description="user name" , required=True),
        "password":fields.String(description="user password" ,required=True)
    }
)

@auth_namespace.route("/signUp")
class UserAuth(Resource):
    
    @auth_namespace.expect(signUp_model)
    @auth_namespace.marshal_with(user_model)
    def post(self):
        """
        signup user
        
        """

        # get data from json
        data=request.get_json()

        username=data.get("username")
        email=data.get("email")
        password=data.get("password")
        print(username, email, password)

       

        if User.query.filter_by(username=username).first():
            return {
                "error": "user exixts"
            }, 400
       
        user=User(username=username, email=email, password=generate_password_hash(password))
        user.save()
        return user, 200
    



@auth_namespace.route("/login")
class Login(Resource):
    @auth_namespace.expect(login_model)
    def post(self):

        """
            generate JWT to login user
        """

        data=request.get_json()
        print(data)
        user= User.query.filter_by(username=data.get("username")).first()
        print(user.username)
        print(check_password_hash(user.password, data.get("password")))

        if user is not None and check_password_hash(user.password, data.get("password")):
            print("True")
            access_token=create_access_token(identity=user.username)
            refresh_token=create_refresh_token(identity=user.username)

            response={
                "access_token":access_token,
                "refresh_token":refresh_token
            }

            return response, HTTPStatus.OK
        
        return {"error":"user does not exist"}, HTTPStatus.NOT_FOUND
    



@auth_namespace.route("/refresh")
class RefreshToken(Resource):
    @jwt_required(refresh=True)
    def post(self):
        username=get_jwt_identity()

        if username:

            access_token=create_access_token(identity=username)

            return {'access_token':access_token}, HTTPStatus.OK
        return {"error": "token invalid or not passed"}, HTTPStatus.BAD_REQUEST