
from ..util import db

class UserGenrePreference(db.Model):
    __tablename__ = 'user_genre_preferences'

    preference_id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.user_id'))
    genre = db.Column(db.String())
    created_at = db.Column(db.String())  # You can use a DateTime field

    # Establish relationships with User and Movie
    user = db.relationship('User', backref='genre_preferences', lazy=True)
    movie = db.relationship('Movie', backref='genre_preferences', lazy=True)
