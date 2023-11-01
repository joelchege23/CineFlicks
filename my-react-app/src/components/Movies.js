import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../services/api';

const Movies = () => {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    const fetchMovies = async () => {
      const moviesData = await api.getMovies();
      setMovies(moviesData);
    };

    fetchMovies();
  }, []);

  return (
    <div>
      <h2>Movies</h2>
      <ul>
        {movies.map((movie) => (
          <li key={movie.id}>
            <Link to={`/movies/${movie.id}`}>
              <p>Title: {movie.title}</p>
              <p>Genre: {movie.genre}</p>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Movies;
