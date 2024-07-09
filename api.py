from flask import Flask, jsonify, request
import random
import numpy as np
import time

app = Flask(__name__)

def generate_data(id):
    data = {
        'router_id': id,
        'timestamp': int(time.time()),
        'cpu_usage': random.uniform(0, 100),
        'memory_usage': random.uniform(0, 100),
        "kind": "string",
        "in-errors": random.randint(0, 100),
        "in-packet-drops": random.randint(0, 50),
        "in-current-packets": random.randint(1000, 5000),
        "in-packet-rate-bps": round(np.random.uniform(10000, 50000), 2),
        "in-packet-rate-pps": round(np.random.uniform(100, 1000), 2),
        "out-errors": random.randint(0, 50),
        "out-packet-drops": random.randint(0, 25),
        "out-current-packets": random.randint(5000, 10000),
        "out-packet-rate-bps": round(np.random.uniform(10000, 50000), 2),
        "out-packet-rate-pps": round(np.random.uniform(500, 2000), 2)
    }
    return data

@app.route('/generate_data/<int:id>', methods=['GET'])
def get_generated_data(id):
    if 0 <= id <= 500:
        data = generate_data(id)
        return jsonify(data)
    else:
        return jsonify({"error": "ID must be between 0 and 500"}), 400

if __name__ == '__main__':
    app.run(debug=True)
