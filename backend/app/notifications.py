import firebase_admin
from firebase_admin import credentials, messaging
from kafka import KafkaProducer
import json

cred = credentials.Certificate('path/to/your/firebase/credentials.json')
firebase_admin.initialize_app(cred)

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def send_notification(user):
    message = messaging.Message(
        notification=messaging.Notification(
            title='Flight Status Update',
            body='Your flight status has been updated.'
        ),
        token=user.preferences['device_token']
    )
    response = messaging.send(message)
    print('Successfully sent message:', response)

    kafka_message = {
        'email': user.email,
        'sms': user.sms,
        'preferences': user.preferences
    }
    producer.send('flight_notifications', json.dumps(kafka_message).encode('utf-8'))
