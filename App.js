import React, { useState, useEffect } from 'react';
import './App.css';
import FlightStatus from './components/FlightStatus';
import NotificationPreferences from './components/NotificationPreferences';

function App() {
  const [flights, setFlights] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/flights')
      .then(response => response.json())
      .then(data => setFlights(data));
  }, []);

  return (
    <div className="App">
      <h1>Flight Status and Notifications</h1>
      <FlightStatus flights={flights} />
      <NotificationPreferences />
    </div>
  );
}

export default App;
