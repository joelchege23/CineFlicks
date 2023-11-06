import React from "react";
import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import LoginForm from "./LoginForm";
import SignupForm from "./SignupForm";
import Homepage from "./Home";
import Chatroom from "./ChatroomPage";
import Friends from "./friends";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/login" element={<LoginForm />} />
        <Route path="/signup" element={<SignupForm />} />
        <Route path="/chatroom" element={<Chatroom />} />
        <Route path="/friends" element={<Friends />} /> 
      </Routes>
    </Router>
  );
}

export default App;
