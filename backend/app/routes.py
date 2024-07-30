from flask import Blueprint, request, jsonify
from app import db, mongo_db
from app.models import User, Flight
from app.notifications import send_notification

main = Blueprint('main', __name__)

@main.route('/api/flights', methods=['GET'])
def get_flights():
    flights = mongo_db.flights.find()
    return jsonify([flight for flight in flights])

@main.route('/api/notifications', methods=['POST'])
def save_preferences():
    data = request.get_json()
    user = User(email=data['email'], sms=data.get('sms'), preferences=data)
    db.session.add(user)
    db.session.commit()
    send_notification(user)
    return jsonify({'message': 'Preferences saved successfully'})
