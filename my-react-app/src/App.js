import React from 'react';
import { BrowserRouter as Router, Route, } from 'react-router-dom';
import Navbar from './Navbar';
import Home from './Home';
import Movies from './Movies';
import MovieDetails from './MovieDetails';
import Reviews from './Reviews';
import ReviewDetails from './ReviewDetails';
import SignUp from './SignUp'; 



function App() {
  return (

      <div>
        <Navbar />

        <Router>
          <Route exact path="/">
            <Home />
          </Route>
          <Route exact path="/movies">
            <Movies />
          </Route>
          <Route path="/movies/:id">
            <MovieDetails />
          </Route>
          <Route exact path="/reviews">
            <Reviews />
          </Route>
          <Route path="/reviews/:id">
            <ReviewDetails />
          </Route>
          <Route path="/signup">
            <SignUp />
          </Route>
        </Router>
      </div>

  );
}

export default App;
