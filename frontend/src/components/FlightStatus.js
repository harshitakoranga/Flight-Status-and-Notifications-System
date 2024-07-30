import React, { useState, useEffect } from 'react';

function FlightStatus() {
  const [flights, setFlights] = useState([]);

  useEffect(() => {
    fetch('/api/flights')
      .then(response => response.json())
      .then(data => setFlights(data));
  }, []);

  return (
    <div>
      <h2>Flight Status</h2>
      <ul>
        {flights.map(flight => (
          <li key={flight.id}>
            {flight.number} - {flight.status} - {flight.gate}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default FlightStatus;
