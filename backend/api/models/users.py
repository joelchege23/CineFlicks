import datetime
from ..util import db


class User(db.Model):
    __tablename__ = 'users'

    

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False) 
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)  # Use SQLite-specific DATETIME('now')
    updated_at = db.Column(db.DateTime(), onupdate=datetime.datetime.utcnow)

    #define relationship between user and messages
    user_messages = db.relationship('Messages', backref='user', lazy='dynamic')
    
    #define relationship between user and friends
    user_friends = db.relationship('Hub', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}| email: {self.email}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()