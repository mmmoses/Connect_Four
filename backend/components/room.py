from components.board import Board
import datetime


class Room:
    def __init__(self, player, gameID, isRed):
        self.player = player
        self.gameID = gameID
        self.isRed = isRed
        self.game = Board(self.player, isRed)
        self.timeCreated = datetime.datetime.now()
