
import datetime
from ..util import db

class ChatRoom(db.Model):
    __tablename__ = 'chatrooms'


    id = db.Column(db.Integer(), primary_key=True)
    chatroom_name = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)   # Use SQLite-specific DATETIME('now')
    updated_at = db.Column(db.DateTime(), onupdate=datetime.datetime.utcnow)

    #define relationship between chatroom and messages
    chatroom_messages = db.relationship('Messages', backref='chatroom', lazy='dynamic')

    def __repr__(self):
        return f'<Chatroom {self.chatroom_name}>' 
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()