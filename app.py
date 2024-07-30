from flask import Flask, jsonify, request
from flask_cors import CORS
from models import Flight
from notifications import send_notification

app = Flask(__name__)
CORS(app)

flights = [
    {"id": 1, "number": "AA101", "status": "On Time", "gate": "A1"},
    {"id": 2, "number": "BA202", "status": "Delayed", "gate": "B2"},
    # Add more mock flights here
]

@app.route('/api/flights', methods=['GET'])
def get_flights():
    return jsonify(flights)

@app.route('/api/notifications', methods=['POST'])
def notify():
    data = request.get_json()
    send_notification(data)
    return jsonify({"message": "Notification sent!"}), 200

if __name__ == '__main__':
    app.run(debug=True)

