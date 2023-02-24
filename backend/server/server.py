# Import flask and datetime module for showing date and time
from doctest import FAIL_FAST
from pickle import TRUE
import random
from flask import Flask, jsonify, request, url_for, redirect
import datetime
from components.user import User
from components.room import Room
import json


# Initializing flask app
app = Flask(__name__)

list_users = []
list_rooms = []


# route for setting username
@app.route('/signup', methods=["POST"])
def signup():
    data = request.get_json()  # of format {"username" : "john"}
    username = data["username"]

    for user in list_users:
        if username == user.name:
            return jsonify(isError=True, message="Username already exists", statusCode=400), 400

    temp_user = User(username)
    list_users.append(temp_user)
    return jsonify(isError=False, message="Success", statusCode=200), 200

@app.route('/   ', methods=["POST"])
def signup():
    data = request.get_json()  # of format {"username" : "john"}
    username = data["username"]

    for user in list_users:
        if username == user.name:
            return jsonify(isError=True, message="Username already exists", statusCode=400), 400

    temp_user = User(username)
    list_users.append(temp_user)
    return jsonify(isError=False, message="Success", statusCode=200), 200


# Running app
if __name__ == '__main__':
    app.run(debug=True)
