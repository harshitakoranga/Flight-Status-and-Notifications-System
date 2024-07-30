import React, { useState } from 'react';
import './NotificationPreferences.css';

function NotificationPreferences() {
  const [type, setType] = useState('');
  const [flightId, setFlightId] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('http://localhost:5000/api/notifications', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ type, flightId })
    })
    .then(response => response.json())
    .then(data => {
      alert(data.message);
    });
  };

  return (
    <div className="notification-preferences">
      <h2>Notification Preferences</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Type:</label>
          <input type="text" value={type} onChange={(e) => setType(e.target.value)} />
        </div>
        <div>
          <label>Flight ID:</label>
          <input type="text" value={flightId} onChange={(e) => setFlightId(e.target.value)} />
        </div>
        <button type="submit">Send Notification</button>
      </form>
    </div>
  );
}

export default NotificationPreferences;
