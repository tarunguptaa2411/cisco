import time
import random
import json
from kafka import KafkaProducer
import requests

# Function to serialize data to JSON
def json_serializer(data):
    return json.dumps(data).encode('utf-8')

# Initialize the Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],  # Replace with your Kafka server address
    value_serializer=json_serializer  # Use the serializer function for JSON
)

while True:
    for router in range(5):
        try:
            # Fetch metrics from the endpoint
            response = requests.get(f'http://localhost:5000/generate_data/{router}')
            response.raise_for_status()  # Raise an exception for HTTP errors
            metrics = response.json()  # Parse the JSON response

            # Send metrics to Kafka
            producer.send('router_metrics', metrics)
            print(f"Sent metrics: {metrics}")

        except requests.RequestException as e:
            print(f"Failed to fetch metrics from router {router}: {e}")

    time.sleep(5)  # Send metrics every 5 seconds