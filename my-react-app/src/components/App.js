import React from "react";
import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import SignupForm from "./SignupForm";
import Homepage from "./Home";
import Cineflix from "./Cineflix";
import Hub from "./Hub";
import AuthForm from "./AuthForm";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/Auth" element={<AuthForm />} />
        <Route path="/signup" element={<SignupForm />} />
        <Route path="/cineflix" element={<Cineflix />} />
        <Route path="/Hub" element={<Hub />} /> 
      </Routes>
    </Router>
  );
}

export default App;