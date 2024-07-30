from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    sms = db.Column(db.String(20), unique=True, nullable=True)
    preferences = db.Column(db.JSON, nullable=False)

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    gate = db.Column(db.String(10), nullable=False)
