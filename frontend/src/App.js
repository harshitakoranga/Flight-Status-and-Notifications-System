import React from 'react';
import FlightStatus from './components/FlightStatus';
import NotificationPreferences from './components/NotificationPreferences';

function App() {
  return (
    <div className="App">
      <h1>Flight Status and Notifications</h1>
      <FlightStatus />
      <NotificationPreferences />
    </div>
  );
}

export default App;
