import React, { useState } from "react";
import axios from "axios";

function SignupForm() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSignup = (e) => {
    e.preventDefault();

    // Send a POST request to your backend to create a new user
    axios
      .post("http://127.0.0.1:5000/auth/signUp", {
        username,
        email,
        password, // You may need to add password to the request body
      })
      .then((response) => {
        // Handle successful sign-up, e.g., show a success message or redirect
        console.log("User created:", response.data);
      })
      .catch((error) => {
        // Handle sign-up error, e.g., display an error message
        console.error("Sign-up failed:", error);
      });
  };

  return (
    <div className="max-w-sm mx-auto mt-8 bg-white p-6 rounded shadow-md">
        <h2 className="text-2xl font-bold mb-4">Sign Up</h2>
        <form onSubmit={handleSignup}>
          <div className="mb-4">
            <label htmlFor="username" className="block text-gray-700 text-sm font-bold mb-2">Username:</label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={handleUsernameChange}
              className="w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-400"
            />
          </div>
          <div className="mb-4">
            <label htmlFor="email" className="block text-gray-700 text-sm font-bold mb-2">Email:</label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={handleEmailChange}
              className="w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-400"
            />
          </div>
          <div className="mb-4">
            <label htmlFor="password" className="block text-gray-700 text-sm font-bold mb-2">Password:</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={handlePasswordChange}
              className="w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-400"
            />
          </div>
          <button
            type="submit"
            className="w-full bg-blue-400 text-white py-2 px-4 rounded-md hover:bg-blue-500 focus:outline-none"
          >
            Sign Up
          </button>
        </form>
      </div>
  );
}

export default SignupForm;
