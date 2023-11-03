from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource,  Namespace, fields
from http import HTTPStatus

from ..models.messages import Messages


messages_namespace = Namespace("messages", "endpoints for messages")

message_model = messages_namespace.model('Messages', {
    'id': fields.Integer(description='The unique identifier of the message'),
    'message_content': fields.String(description='Content of the message'),
    'chatroom_id': fields.Integer(description='ID of the chatroom associated with the message'),
    'user_id': fields.Integer(description='ID of the user who sent the message'),
    'created_at': fields.DateTime(description='Date and time the message was created'),
    'updated_at': fields.DateTime(description='Date and time the message was last updated'),
})

@messages_namespace.route('/messages')
class MessagesResource(Resource):
    @messages_namespace.marshal_list_with(message_model)
    @jwt_required()
    def get(self):
        """Get all messages"""
        messages = Messages.query.all()
        return messages, HTTPStatus.OK

    @messages_namespace.expect(message_model)
    @messages_namespace.marshal_with(message_model, code=201)
    @jwt_required()
    def post(self):
        """Create a message"""
        data = request.get_json()
        new_message = Messages(
            message_content=data.get('message_content'),
            chatroom_id=data.get('chatroom_id'),
            user_id=data.get('user_id')
        )
        new_message.save()
        return new_message, HTTPStatus.CREATED

@messages_namespace.route('/messages/<int:id>')
class MessageByIdResource(Resource):
    @messages_namespace.marshal_with(message_model)
    @jwt_required()
    def get(self, id):
        """Get a message by its ID"""
        message = Messages.query.get(id)
        if message:
            return message, HTTPStatus.OK
        return {"message": "Message not found"}, HTTPStatus.NOT_FOUND

    @jwt_required()
    def delete(self, id):
        """Delete a message by its ID"""
        message = Messages.query.get(id)
        if message:
            message.delete()
            return {"message": "Message deleted"}, HTTPStatus.NO_CONTENT
        return {"message": "Message not found"}, HTTPStatus.NOT_FOUND