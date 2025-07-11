import csv
import time
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'nyc_taxi_data'

with open('raw_data/yellow_tripdata_sample.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        producer.send(topic, value=row)
        print(f"Sent: {row}")
        time.sleep(1)  # simulate real-time
