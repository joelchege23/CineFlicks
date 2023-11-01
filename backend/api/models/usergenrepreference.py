
from ..util import db

class UserGenrePreference(db.Model):
    __tablename__ = 'user_genre_preferences'

    preference_id = db.Column(db.Integer(), primary_key=True)
    # user_id = db.Column(db.Integer(), db.ForeignKey('user.user_id'))
    genre = db.Column(db.String())
    created_at = db.Column(db.String())  # You can use a DateTime field

    # # Establish relationships with User and Movie
    # user = db.relationship('User', backref='user_genre_preferences', lazy=True)
    # movie = db.relationship('Movie', backref='movie_genre_preferences', lazy=True ,overlaps="genre_preferences")
    
    # Define the foreign key relationship to associate the user_genre_preference with a movie
    # movie_id = db.Column(db.Integer(), db.ForeignKey('movie.movie_id'))
