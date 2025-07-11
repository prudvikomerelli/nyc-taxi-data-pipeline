import json
import pandas as pd
from kafka import KafkaProducer
import time

# Kafka config
KAFKA_BROKER = 'localhost:9092'  # Change if using Docker networking
TOPIC = 'nyc_taxi'

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic} partition {msg.partition}')

def main():
    # Read parquet file
    df = pd.read_parquet('sample_data/yellow_tripdata_2023-01.parquet')

    # Initialize Kafka producer
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        linger_ms=10
    )

    print(f'Starting to send {len(df)} messages to topic "{TOPIC}"')

    for i, row in df.iterrows():
        data = {
            'vendor_id': row['VendorID'],
            'pickup_datetime': str(row['tpep_pickup_datetime']),
            'dropoff_datetime': str(row['tpep_dropoff_datetime']),
            'passenger_count': int(row['passenger_count']),
            'trip_distance': float(row['trip_distance']),
            'rate_code': row['RatecodeID'],
            'payment_type': row['payment_type'],
            'total_amount': float(row['total_amount'])
        }

        producer.send(TOPIC, value=data)
        producer.flush()
        time.sleep(0.01)  # simulate streaming, 10ms delay

    print('All messages sent.')
    producer.close()

if __name__ == '__main__':
    main()
