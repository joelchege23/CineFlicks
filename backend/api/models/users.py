from ..util import db


class User(db.Model):
    __tablename__ = 'user'

    user_id =db. Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())  # Store hashed passwords
    created_at = db.Column(db.String())  # You can use a DateTime field

    # Establish relationships with User-Movie Ratings and User-Genre Preferences
    ratings = db.relationship('UserMovieRating', backref='user', lazy=True)
    genre_preferences = db.relationship('UserGenrePreference', backref='user', lazy=True)

    comments = db.relationship('Comment', backref='user', lazy=True)