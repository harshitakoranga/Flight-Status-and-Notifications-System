from flask import Flask, jsonify, request
from models import db, Flight
from notifications import send_notification

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flights.db'
db.init_app(app)

@app.route('/api/flights', methods=['GET'])
def get_flights():
    flights = Flight.query.all()
    return jsonify([flight.to_dict() for flight in flights])

@app.route('/api/notifications', methods=['POST'])
def send_notifications():
    data = request.json
    send_notification(data['flight_id'], data['message'])
    return jsonify({"status": "Notification sent"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
