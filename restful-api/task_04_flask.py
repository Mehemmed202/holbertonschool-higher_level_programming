#!/usr/bin/python3

from flask import Flask, jsonify, reuest

app = Flask(__name__)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

@app.route("/status")
def get_status():
    return "OK"

@app.route("/users/<username>")
def get_user():
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods = ["POST"])
def add_user():
    data = requests.get_json(silent=True)

    if data is None:
        return jsonify({"error":"Invalid JSON"}), 400

    if username is None:
        return jsonify({"error":"Username is required"}), 400

    if username in users:
        return jsonify({"error":"Username already exists"}), 409

if __name__ == "__main__":
    app.run()
