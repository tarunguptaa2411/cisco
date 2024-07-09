from kafka import KafkaConsumer
import json
from prometheus_client import start_http_server, Gauge
import time
import random
import numpy as np

# Function to deserialize data from JSON
def json_deserializer(data):
    return json.loads(data.decode('utf-8'))

# Initialize Kafka consumer
consumer = KafkaConsumer(
    'router_metrics',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='router_group',
    value_deserializer=json_deserializer
)

# Initialize Prometheus metrics with labels
cpu_usage = Gauge('cpu_usage', 'CPU usage metric', ['router_id'])
memory_usage = Gauge('memory_usage', 'Memory usage metric', ['router_id'])
in_errors = Gauge('in_errors', 'Inbound errors', ['router_id'])
in_packet_drops = Gauge('in_packet_drops', 'Inbound packet drops', ['router_id'])
in_current_packets = Gauge('in_current_packets', 'Inbound current packets', ['router_id'])
in_packet_rate_bps = Gauge('in_packet_rate_bps', 'Inbound packet rate (bps)', ['router_id'])
in_packet_rate_pps = Gauge('in_packet_rate_pps', 'Inbound packet rate (pps)', ['router_id'])
out_errors = Gauge('out_errors', 'Outbound errors', ['router_id'])
out_packet_drops = Gauge('out_packet_drops', 'Outbound packet drops', ['router_id'])
out_current_packets = Gauge('out_current_packets', 'Outbound current packets', ['router_id'])
out_packet_rate_bps = Gauge('out_packet_rate_bps', 'Outbound packet rate (bps)', ['router_id'])
out_packet_rate_pps = Gauge('out_packet_rate_pps', 'Outbound packet rate (pps)', ['router_id'])

# Function to process Kafka messages and update Prometheus metrics
def process_message(metrics):
    router_id = metrics['router_id']
    cpu_usage.labels(router_id=router_id).set(metrics['cpu_usage'])
    memory_usage.labels(router_id=router_id).set(metrics['memory_usage'])
    in_errors.labels(router_id=router_id).set(metrics['in-errors'])
    in_packet_drops.labels(router_id=router_id).set(metrics['in-packet-drops'])
    in_current_packets.labels(router_id=router_id).set(metrics['in-current-packets'])
    in_packet_rate_bps.labels(router_id=router_id).set(metrics['in-packet-rate-bps'])
    in_packet_rate_pps.labels(router_id=router_id).set(metrics['in-packet-rate-pps'])
    out_errors.labels(router_id=router_id).set(metrics['out-errors'])
    out_packet_drops.labels(router_id=router_id).set(metrics['out-packet-drops'])
    out_current_packets.labels(router_id=router_id).set(metrics['out-current-packets'])
    out_packet_rate_bps.labels(router_id=router_id).set(metrics['out-packet-rate-bps'])
    out_packet_rate_pps.labels(router_id=router_id).set(metrics['out-packet-rate-pps'])

# Start Prometheus HTTP server
start_http_server(8000)  # Replace with the port number you want to expose metrics on

# Consume messages from Kafka and update Prometheus metrics
for message in consumer:
    metrics = message.value
    process_message(metrics)
    print(f"Received from Kafka and processed: {metrics}")

# Optionally, keep the program running to serve Prometheus metrics
