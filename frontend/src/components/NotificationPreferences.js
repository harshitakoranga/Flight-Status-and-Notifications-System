import React, { useState } from 'react';

function NotificationPreferences() {
  const [email, setEmail] = useState('');
  const [sms, setSms] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    fetch('/api/notifications', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, sms }),
    });
  };

  return (
    <div>
      <h2>Notification Preferences</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Email:
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
        </label>
        <br />
        <label>
          SMS:
          <input type="text" value={sms} onChange={(e) => setSms(e.target.value)} />
        </label>
        <br />
        <button type="submit">Save Preferences</button>
      </form>
    </div>
  );
}

export default NotificationPreferences;
