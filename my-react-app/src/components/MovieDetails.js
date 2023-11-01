import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../services/api';

const MovieDetails = () => {
  const { id } = useParams();
  const [movie, setMovie] = useState(null);

  useEffect(() => {
    const fetchMovieDetails = async () => {
      const movieData = await api.getMovieById(id);
      setMovie(movieData);
    };

    fetchMovieDetails();
  }, [id]);

  return (
    <div>
      <h2>Movie Details</h2>
      {movie && (
        <div>
          <p>Title: {movie.title}</p>
          <p>Description: {movie.description}</p>
          <p>Release Date: {movie.release_date}</p>
          <p>Genre: {movie.genre}</p>
          {/* Add reviews or other details here */}
        </div>
      )}
    </div>
  );
};

export default MovieDetails;
