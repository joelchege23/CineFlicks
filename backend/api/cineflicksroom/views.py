from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import fields, Namespace, Resource, marshal
from ..models.chatroom import ChatRoom
from ..util import db
from http import HTTPStatus
chatroom_namespace= Namespace("cinflicks-chatroom","endpoints for cineflicks chatroom")

# api blueprint
chatroom_model = chatroom_namespace.model('ChatRoom', {
    'id': fields.Integer(attribute='id', description='The unique identifier of the chatroom'),
    'chatroom_name': fields.String(description='Name of the chatroom'),
    'created_at': fields.DateTime(description='Date and time the chatroom was created'),
    'updated_at': fields.DateTime(description='Date and time the chatroom was last updated'),
})


@chatroom_namespace.route('/chatrooms')
class ChatroomList(Resource):
    @chatroom_namespace.marshal_list_with(chatroom_model)
    @jwt_required()
    def get(self):
        """get all available chatrooms"""
        chatrooms = ChatRoom.query.all()
        return chatrooms, HTTPStatus.OK

    @chatroom_namespace.expect(chatroom_model)
  
    @jwt_required()
    def post(self):
        """create chatroom"""
        data = request.get_json()
        if data:
            try:
                if not ChatRoom.query.filter_by(chatroom_name=data.get("chatroom_name")).exists():
                    new_chatroom = ChatRoom(chatroom_name=data.get('chatroom_name'))
                    new_chatroom.save()
                    return marshal(new_chatroom, chatroom_model, skip_none=True), HTTPStatus.CREATED
                return {"error":"chatroom exists"}, HTTPStatus.BAD_REQUEST
        
            except:
                return {"error":"validation errors"}, HTTPStatus.BAD_GATEWAY
        return {"error":"no data has been passed"}, HTTPStatus.BAD_REQUEST
    


@chatroom_namespace.route('/chatrooms/<int:id>')
class ChatroomById(Resource):
    @jwt_required()
    def get(self, id):
        """Get a chatroom by its ID"""
        chatroom = ChatRoom.query.get(id)
        if chatroom:
            return marshal(chatroom, chatroom_model, skip_none=True), HTTPStatus.OK
        return {"error": "Chatroom not found"}, HTTPStatus.NOT_FOUND


    @chatroom_namespace.expect(chatroom_model)
    @jwt_required()
    def patch(self, id):
        """Update a chatroom by its ID"""
        chatroom = ChatRoom.query.get(id)
        if chatroom:
            data = request.get_json()
            for attr in data:
                setattr(chatroom, attr, data.get(f'{attr}'))

            chatroom.save()
            return marshal(chatroom, chatroom_model, skip_none=True), HTTPStatus.OK
        return {"error": "Chatroom not found"}, HTTPStatus.NOT_FOUND

    @jwt_required()
    def delete(self, id):
        """Delete a chatroom by its ID"""
        chatroom = ChatRoom.query.get(id)
        if chatroom:
            chatroom.delete()
            return {"message": "Chatroom deleted"}, HTTPStatus.NO_CONTENT
        return {"error": "Chatroom not found"}, HTTPStatus.NOT_FOUND