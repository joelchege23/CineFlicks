import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function AuthForm() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isLoginMode, setIsLoginMode] = useState(true);
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);

 
  const navigate = useNavigate();

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);

    try {
      if (isLoginMode) {
       
        const response = await axios.post("http://127.0.0.1:5000/auth/login", { username, password });
        console.log("Login successful:", response.data);
        navigate("/chatroom");
      } else {
        
        const response = await axios.post("http://127.0.0.1:5000/auth/signUp", { username:username, email:email, password_hash:password });
        console.log("User created:", response.data);
        navigate("/chatroom");
      }
    } catch (error) {
      setError("Login or sign-up failed. Please check your information.");
    } finally {
      setIsLoading(false);
    }
  };

  const toggleMode = () => {
    setIsLoginMode((prevMode) => !prevMode);
  };

  return (
    <div className="bg-blue-500 min-h-screen flex items-center justify-center">
      <div className="max-w-sm mx-auto mt-8 bg-white p-6 rounded shadow-md">
        <h2 className="text-2xl font-bold mb-4">{isLoginMode ? "Login" : "Sign Up"}</h2>
        <form onSubmit={handleFormSubmit}>
          <div className="mb-4">
            <label htmlFor="username" className="block text-gray-700 text-sm font-bold mb-2">
              Username:
            </label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={handleUsernameChange}
              className="w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-400"
            />
          </div>
          {!isLoginMode && (
            <div className="mb-4">
              <label htmlFor="email" className="block text-gray-700 text-sm font-bold mb-2">
                Email:
              </label>
              <input
                type="email"
                id="email"
                value={email}
                onChange={handleEmailChange}
                className="w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-400"
              />
            </div>
          )}
          <div className="mb-4">
            <label htmlFor="password" className="block text-gray-700 text-sm font-bold mb-2">
              Password:
            </label>
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
            disabled={isLoading}
          >
            {isLoading ? (
              <div role="status" className="inline-block mr-2">
                <svg
                  aria-hidden="true"
                  className="animate-spin"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 100 101"
                  fill="none"
                >
                  <path
                    d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                    fill="currentColor"
                  />
                  <path
                    d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                    fill="currentFill"
                  />
                </svg>
                <span className="sr-only">Loading...</span>
              </div>
            ) : (
              isLoginMode ? "Log In" : "Sign Up"
            )}
          </button>
        </form>
        <p className="mt-2 text-blue-500 cursor-pointer" onClick={toggleMode}>
          {isLoginMode ? "Don't have an account? Sign Up" : "Already have an account? Log In"}
        </p>
        {error && <p className="text-red-500 mt-2">{error}</p>}
      </div>
    </div>
  );
}

export default AuthForm;
