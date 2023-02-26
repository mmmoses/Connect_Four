from flask import Flask, jsonify, request, url_for, redirect
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_cors import CORS
from doctest import FAIL_FAST
from pickle import TRUE
import random
import datetime
from components.user import User
from components.room import Room
from components.room_manager import RoomManager
from components.user_manager import UserManager
import json


# Initializing flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def index():
    return 'Hello, World!'


"""""
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
"""""

room_manager = RoomManager()
user_manager = UserManager()


@app.route('/signup', methods=["POST"])
def signup():
    data = request.get_json()
    username = data["name"]

    if user_manager.check_existing(username):
        return jsonify(isError=True, message="Username already exists", statusCode=409), 409

    user_manager.add_new_user(username)
    return jsonify(isError=False, message="Successfull signed up", statusCode=200), 200


@socketio.on('create-room')
def create_game():
    data = request.get_json()
    player = User(data['name'])
    room = room_manager.create_room(player)
    join_room(room.gameID)
    emit('created', {'game_id': room.gameID}, room=room.gameID)


@socketio.on('join')
def join_game():
    data = request.get_json()
    game_id = data['game_id']
    room = room_manager.get_room(game_id)
    if room is not None:
        join_room(game_id)
        emit('viewer', {'game_id': game_id}, room=game_id)
    else:
        emit('not_found', {'game_id': game_id}, room=request.sid)


@socketio.on('leave')
def leave_game():
    data = request.get_json()
    game_id = data['game_id']
    leave_room(game_id)
    emit('left', {'game_id': game_id}, room=game_id)


@socketio.on('move')
def make_move():
    data = request.get_json()
    game_id = data['game_id']
    room = room_manager.get_room(game_id)

    if room is not None:
        col = data['col']
        row = room.game.get_available_locations()[str(col)]
        if row is not None:
            result = room.game.place_piece(col)
            emit('moved', {
                'game_id': game_id,
                'col': col,
                'row': row,
                'player': room.game.user.name,
                'bot_col': result['bot_col'],
                'bot_row': result['bot_row'],
                'bot_won': result['bot_won'],
                'user_won': result['user_won'],
            }, room=game_id)
        else:
            emit('invalid_move', {'game_id': game_id}, room=request.sid)
    else:
        emit('not_found', {'game_id': game_id}, room=request.sid)


# Running app
if __name__ == '__main__':
    socketio.run(app, debug=True, port=5001)
