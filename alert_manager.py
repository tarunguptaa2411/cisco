from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/alert', methods=['GET'])
def receive_alert():
    if request.is_json:
        alert = request.get_json()
        print("Received alert:", alert)
        # Here you can add code to process the alert, e.g., logging, forwarding, etc.
        return jsonify({"status": "success", "message": "Alert received"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid request"}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=45678)
