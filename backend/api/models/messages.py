import datetime
from ..util import db


class Messages(db.Model):
    __tablename__ ='messages'

    id = db.Column(db.Integer, primary_key=True)
    message_content = db.Column(db.String())
    chatroom_id = db.Column(db.Integer, db.ForeignKey('chatrooms.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)   # Use SQLite-specific DATETIME('now') 
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)    

    def __repr__(self):
        return f'<Message {self.message_content}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

