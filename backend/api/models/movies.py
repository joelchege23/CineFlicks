from ..util import db


class Movie(db.Model):
    __tablename__ = 'movie'

    movie_id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(),  nullable=False)
    description = db.Column(db.String())
    release_year = db.Column(db.Integer())
    genre = db.Column(db.String())
    director = db.Column(db.String())
    rating = db.Column(db.Integer())  # You can use a Float for a more precise rating
    runtime = db.Column(db.Integer())
    poster = db.Column(db.String())  # Store the URL or path to the movie's poster

    # Establish relationships with User-Movie Ratings and User-Genre Preferences
    ratings = db.relationship('UserMovieRating', backref='movie' , lazy=True)
    genre_preferences = db.relationship('UserGenrePreference', backref='movie', lazy=True)

    # Establish a one-to-many relationship with comments
    comments = db.relationship('Comment', back_populates='movie')

