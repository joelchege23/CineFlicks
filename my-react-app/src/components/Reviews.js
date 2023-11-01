import React from 'react';
import { Link } from 'react-router-dom';

const Reviews = () => {

  return (
    <div>
      <h2>Reviews</h2>
      {/* Display a list of reviews */}
      <ul>
        <li>
          <Link to="/reviews/1">
            <p>Rating: 4</p>
            <p>Comment: Great movie!</p>
          </Link>
        </li>
        {/* Add more review items as needed */}
      </ul>
    </div>
  );
};

export default Reviews;
