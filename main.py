# # from flask import Flask, jsonify
# from flask import Flask, jsonify, request
# import random
# import numpy as np
# import pandas as pd
#
# app = Flask(__name__)
#
#
# # @app.route('/api/data', methods=['GET'])
# @app.route('/')
# def get_data():
#     data_points = []
#     for id in range(1, 1001):  # Generate data for ids from 1 to 1000
#         random.seed(id)  # Ensure consistent random data for each id
#         data = {
#             "id": id,
#             "Property Type": "Object",
#             "Description": "Object type. Has the fixed value 'object#interface-statistics'",
#             "kind": "string",
#             "if-name": f"interface-{id}",
#             "in-errors": random.randint(0, 100),
#             "in-packet-drops": random.randint(0, 50),
#             "in-current-packets": random.randint(1000, 5000),
#             "in-packet-rate-bps": round(np.random.uniform(10000, 50000), 2),
#             "in-packet-rate-pps": round(np.random.uniform(100, 1000), 2),
#             "out-errors": random.randint(0, 50),
#             "out-packet-drops": random.randint(0, 25),
#             "out-current-packets": random.randint(5000, 10000),
#             "out-packet-rate-bps": round(np.random.uniform(50000, 100000), 2),
#             "out-packet-rate-pps": round(np.random.uniform(500, 2000), 2)
#         }
#         data_points.append(data)
#
#     return jsonify(data_points)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
# #
# # app = Flask(__name__)
# #
# # @app.route('/')
# # def home():
# #     return "Welcome to the API!"
# #
# # if __name__ == '__main__':
# #     app.run(debug=True)


from flask import Flask, jsonify, request
import random
import numpy as np

app = Flask(__name__)

def generate_data(id):
    data = {
        "id": id,
        "Property Type": "Object",
        "Description": "Object type. Has the fixed value 'object#interface-statistics'",
        "kind": "string",
        "if-name": f"interface-{id}",
        "in-errors": random.randint(0, 100),
        "in-packet-drops": random.randint(0, 50),
        "in-current-packets": random.randint(1000, 5000),
        "in-packet-rate-bps": round(np.random.uniform(10000, 50000), 2),
        "in-packet-rate-pps": round(np.random.uniform(100, 1000), 2),
        "out-errors": random.randint(0, 50),
        "out-packet-drops": random.randint(0, 25),
        "out-current-packets": random.randint(5000, 10000),
        "out-packet-rate-bps": round(np.random.uniform(50000, 100000), 2),
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
