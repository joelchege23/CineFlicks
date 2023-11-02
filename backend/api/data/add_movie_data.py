from ..models.movies import Movie
from ..util import db

# Define data for a new movie

new_movie = Movie(
    title="Sample Movie",
    description="This is a sample movie.",
    release_year=2023,
    genre="Action",
    director="John Doe",
    rating=8.5,
    runtime=120,
    poster="https://example.com/sample_movie_poster.jpg"
)

# Add the new movie to the database session and commit the changes
db.session.add(new_movie)
db.session.commit()

# You can add more movies using the same approach
