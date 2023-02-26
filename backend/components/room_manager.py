from components.room import Room
import random


class RoomManager:
    def __init__(self):
        self.rooms = {}

    def create_room(self, player):
        game_id = random.randint(1000, 9999)
        is_red = random.choice([True, False])
        room = Room(player, game_id, is_red)
        self.rooms[game_id] = room
        return room

    def get_room(self, game_id):
        return self.rooms.get(game_id)
