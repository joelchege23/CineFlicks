
import datetime
from ..util import db

class ChatRoom(db.Model):
    __tablename__ = 'chatrooms'


    id = db.Column(db.Integer(), primary_key=True)
    chatroom_name = db.Column(db.String(20))
    created_at = db.Column(db.DateTime(), server_default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())

    #define relationship between chatroom and messages
    chatroom_messages = db.relationship('Message', backref='chatroom', lazy='dynamic')

    def __repr__(self):
        return f'<Chatroom {self.chatroom_name}>' 