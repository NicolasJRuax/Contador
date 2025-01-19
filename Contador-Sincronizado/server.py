# server.py
from flask import Flask, request, jsonify
from threading import Lock

app = Flask(__name__)

# Contador global
counter = 0

# Lock para asegurar exclusión mutua
counter_lock = Lock()

@app.route("/value", methods=["GET"])
def get_value():
    global counter
    return jsonify({"counter": counter})

@app.route("/increment", methods=["POST"])
def increment():
    global counter
    # Aseguramos exclusión mutua
    with counter_lock:
        counter += 1
        return jsonify({"counter": counter})

@app.route("/reset", methods=["POST"])
def reset():
    global counter
    with counter_lock:
        counter = 0
        return jsonify({"counter": counter})

if __name__ == "__main__":
    # Se lanza el servidor en el puerto 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
