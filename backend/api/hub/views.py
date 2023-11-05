from http import HTTPStatus
from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields, marshal

from ..models.hub import Hub

from ..models.users import User


hub_namespace=Namespace("hub", "hub endpoint")

hub_model = hub_namespace.model('hub', {
    'id': fields.Integer(description='The unique identifier of the friend'),
    'user_id': fields.Integer(description='The user ID of the friend'),
    'hubfriend_id': fields.Integer(description='The user ID of the friend'),
})

@hub_namespace.route('/users/<int:user_id>/hub')
class UserhubResource(Resource):
   
    @jwt_required()
    def get(self, user_id):
        """Get user hub"""
        user = User.query.get(user_id)
        if user is None:
            return {"message": "User not found"}, HTTPStatus.NOT_FOUND

        hubfriend = Hub.query.filter_by(user_id=user_id).all()

        friend_list = [{"hubfriend_id": friend.id, "friend_name": friend.user.username} for friend in hubfriend]

        if len(friend_list) > 0:

            return {"user_id": user.id, "username": user.username, "friends": friend_list} , HTTPStatus.OK
        else :
            return {"message":"No friends for this user"} ,HTTPStatus.NO_CONTENT
        


        
    @jwt_required()
    @hub_namespace.expect(hub_model)
    def post(self, user_id):
        """Add a friend to the user's hub"""
        data = request.get_json()
        hubfriend_id = data.get("hubfriend_id")

        # Check if the hub friend exists
        hubfriend = User.query.filter_by(id=hubfriend_id).first()
        if not hubfriend:
            return {"error": "Hub friend not found"}, HTTPStatus.NOT_FOUND

        # Check if the user is trying to add themselves as a hub friend
        if user_id == hubfriend_id:
            return {"error": "You cannot add yourself as a hub friend"}, HTTPStatus.BAD_REQUEST

        # Check if the user is already friends with the hub friend
        existing_hub = Hub.query.filter_by(user_id=user_id, hubfriend_id=hubfriend_id).first()
        if existing_hub:
            return {"error": "You are already friends with this user"}, HTTPStatus.BAD_REQUEST

        hub = Hub(user_id=user_id, hubfriend_id=hubfriend_id)
        hub.save()

        return marshal(hub, hub_model , skip_none=True),  HTTPStatus.CREATED