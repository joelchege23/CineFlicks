import datetime
from ..util import db


class User(db.Model):
    __tablename__ = 'user'

    user_id =db. Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(1000), nullable=False)  # Store hashed passwords
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)  # You can use a DateTime field

    # Establish relationships with User-Movie Ratings and User-Genre Preferences
    # ratings = db.relationship('UserMovieRating', backref='user_ratings', lazy=True)
    # genre_preferences = db.relationship('UserGenrePreference', backref='user_genres', lazy=True)

    # comments = db.relationship('Comment', backref='user_comments', lazy=True)


    def save(self):
        db.session.add(self)
        db.session.commit()