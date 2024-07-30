from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('flight_notifications', bootstrap_servers='localhost:9092', group_id='notification_group')

for message in consumer:
    notification_data = json.loads(message.value)
    print(notification_data)  # Process the notification data (e.g., send email/SMS)
