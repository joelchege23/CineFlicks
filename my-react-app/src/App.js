import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Movies from './components/Movies';
import MovieDetails from './components/MovieDetails';
import Reviews from './components/Reviews';
import ReviewDetails from './components/ReviewDetails';

function App() {
  return (
    <Router>
      <div>
        <Navbar />

        <Switch>
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
        </Switch>
      </div>
    </Router>
  );
}

export default App;
