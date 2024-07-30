from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    gate = db.Column(db.String(5), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'number': self.number,
            'status': self.status,
            'gate': self.gate
        }
