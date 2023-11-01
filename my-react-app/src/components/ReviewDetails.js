import React from 'react';
import { useParams } from 'react-router-dom';

const ReviewDetails = () => {
  const { id } = useParams();

  return (
    <div>
      <h2>Review Details</h2>
      {/* Display details of a specific review */}
      <p>Rating: 4</p>
      <p>Comment: Great movie!</p>
    </div>
  );
};

export default ReviewDetails;
