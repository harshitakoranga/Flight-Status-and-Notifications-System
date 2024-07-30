from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def send_notification(data):
    producer.send('flight_notifications', json.dumps(data).encode('utf-8'))
