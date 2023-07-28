from flask import Flask, jsonify, send_from_directory
import random

app = Flask(__name__)

# Return index file
@app.route("/", methods = ['GET'])
def base():
    return send_from_directory('client/dist', 'index.html')

# Path for all the static files
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/dist', path)

# Simple REST API example to be called from frontend
@app.route("/rand", methods = ['GET'])
def hello():
    data = {
        "num": random.randint(0, 100)
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
