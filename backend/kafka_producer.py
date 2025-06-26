# kafka_producer.py
from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open('data/health_data.json') as f:
    data = json.load(f)

for record in data:
    producer.send('health-topic', value=record)
    print(f"Sent: {record}")
    time.sleep(1)  # simulate stream

producer.flush()
