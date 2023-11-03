import React, { useState, useEffect } from 'react';
import { io } from 'socket.io-client';
import { v4 as uuidv4 } from 'uuid';

const Cineflix = () => {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  const [userId, setUserId] = useState(null);
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    const newSocket = io('https://chatwave-x4y9.onrender.com');
    setSocket(newSocket);

    const generatedUserId = uuidv4();
    setUserId(generatedUserId);

    newSocket.on('connect', () => {
      console.log('Connected to server');
    });

    newSocket.on('new_message', (data) => {
      console.log('Received new message:', data);
      setMessages((prevMessages) => [...prevMessages, data]);
    });

    return () => {
      newSocket.disconnect();
      console.log('Disconnected from server');
    };
  }, []);

  const sendMessage = () => {
    if (socket) {

      const newMessageData = { message_content: newMessage, cineflix_id: 1, user_id: userId };
      socket.emit('new_message', newMessageData);

      console.log('Sent new message:', newMessageData);

      setMessages((prevMessages) => [...prevMessages, newMessageData]);
      setNewMessage('');
    }
  };

  return (
    <div class="bg-blue-400 p-4">
      <div>
        <h2 class="text-white">Cineflix</h2>
        <div>
          {messages.map((message, index) => (
            <div key={index} class="text-white">
              <strong>Message:</strong> {message.message_content}
            </div>
          ))}
        </div>
      </div>
      <div class="mt-4">
        <input
          type="text"
          value={newMessage}
          onChange={(e) => setNewMessage(e.target.value)}
          placeholder="Type your message..."
          class="bg-white p-2 rounded"
        />
        <button
          onClick={sendMessage}
          class="bg-gray-800 text-white px-4 py-2 rounded ml-2"
        >
          Send
        </button>
      </div>
    </div>

  );
};

export default Cineflix;