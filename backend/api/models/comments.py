import datetime
from ..util import db

class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer(), primary_key=True)
    description = db.Column(db.String())
    date_created = db.Column(db.DateTime(), default=datetime.datetime.utcnow)

    # a user is related to a comment
    user_id= db.Column(db.Integer(), db.ForeignKey('user.user_id'))

    movie_id= db.Column(db.Integer(), db.ForeignKey('movie.movie_id'))