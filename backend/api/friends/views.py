from http import HTTPStatus
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from ..models.friends import Friends

from ..models.users import User


friends_namespace=Namespace("friends", "friends endpoint")

friends_model = friends_namespace.model('Friends', {
    'id': fields.Integer(description='The unique identifier of the friend'),
    'user_id': fields.Integer(description='The user ID of the friend'),
    'friend_id': fields.Integer(description='The user ID of the friend'),
})

@friends_namespace.route('/users/<int:user_id>/friends')
class UserFriendsResource(Resource):
    @friends_namespace.marshal_with(friends_model)
    @jwt_required()
    def get(self, user_id):
        """Get user friends"""
        user = User.query.get(user_id)
        if user is None:
            return {"message": "User not found"}, HTTPStatus.NOT_FOUND

        friends = Friends.query.filter_by(user_id=user_id).all()

        friend_list = [{"friend_id": friend.id, "friend_name": friend.user.username} for friend in friends]

        return {"user_id": user.id, "username": user.username, "friends": friend_list} , 