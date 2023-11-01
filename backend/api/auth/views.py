from flask_restx import Namespace, Resource, fields
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from  ..models.users import User
from http import HTTPStatus


auth_namespace=Namespace("auth", "handle user authentication")

signUp_model=auth_namespace.model(
    'User',{
        'username':fields.String(required=True),
        'email':fields.String(required=True),
        'password':fields.String(required=True),

    }
)

user_model=auth_namespace.model(
    'User',{
        'user_id':fields.Integer(),
        'username':fields.String(required=True),
        'email':fields.String(required=True),
        
    }
)

@auth_namespace.route("/signUp")
class UserAuth(Resource):
    @auth_namespace.marshal_with(user_model)
    @auth_namespace.expect(signUp_model)
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
       
        user=User(username=username, email=email, password=password)
        user.save()
        return user, 200