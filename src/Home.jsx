
import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom"; // Import Link from react-router-dom
import LoginForm from "./LoginForm";
        
function Homepage() {
  const [users, setUsers] = useState([]);
        
  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/auth/users")
      .then((response) => {
        setUsers(response.data);
      })
      .catch((error) => {
        console.error("Error fetching users:", error);
      });
  }, []);

return (
  <>
    <div className="bg-white p-4 flex justify-between items-center">
      <h1 className="text-2xl font-bold text-blue-400">CINFLICKS</h1>
      <nav className="flex space-x-4">
        <a href="#" className="text-black">
          Services
        </a>
        <a href="#" className="text-black">
          Help Center
        </a>
      </nav>
    </div>
    <div className="m-12">
      <div className="bg-white min-h-screen">
        <div className="flex flex-col h-screen  justify-between items-center">
          <div className="md:flex  m-5">
            <div className="object-contain image">
              <img
                className="w-full h-auto object-contain"
                src="/cineflicks.jpeg"   

                />

                <div className="text-center md:text-left m-6">
                  <p className="text-4xl md:text-7xl font-bold mb-2 text-blue-400 my-6 py-6">
                  CINFLICKS.
                  </p>
                  {/* Use Link component to navigate to the login page */}
                  <Link
                    to="/login"
                    className="bg-transparent hover:bg-blue-400 text-blue-500 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
                  >
                    LogIn
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
        
export default Homepage;
           