import React from 'react';
import './FlightStatus.css';

function FlightStatus({ flights }) {
  return (
    <div className="flight-status">
      <h2>Flight Status</h2>
      <ul>
        {flights.map(flight => (
          <li key={flight.id}>
            Flight {flight.number} is {flight.status} at gate {flight.gate}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default FlightStatus;
