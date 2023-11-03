from http import HTTPStatus
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from ..models.hub import Hub

from ..models.users import User


hub_namespace=Namespace("hub", "hub endpoint")

hub_model = hub_namespace.model('hub', {
    'id': fields.Integer(description='The unique identifier of the friend'),
    'user_id': fields.Integer(description='The user ID of the friend'),
    'hubhriend_id': fields.Integer(description='The user ID of the friend'),
})

@hub_namespace.route('/users/<int:user_id>/hub')
class UserhubResource(Resource):
    @hub_namespace.marshal_with(hub_model)
    @jwt_required()
    def get(self, user_id):
        """Get user hub"""
        user = User.query.get(user_id)
        if user is None:
            return {"message": "User not found"}, HTTPStatus.NOT_FOUND

        hubfriend = Hub.query.filter_by(user_id=user_id).all()

        friend_list = [{"hubfriend_id": friend.id, "friend_name": friend.user.username} for friend in hubfriend]

        return {"user_id": user.id, "username": user.username, "friends": friend_list} , HTTPStatus.OK