from ..util import db
class Hub(db.Model):
    __tablename__ = 'hubfriends'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)