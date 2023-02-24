import datetime


class User:
    def __init__(self, username):
        self.name = username
        self.gameID = None
        self.__timeCreated = datetime.datetime.now()

    def get_time_created(self):
        return self.__timeCreated

    def get_name(self):
        return self.name

    def get_game(self):
        return self.gameID

    def set_gameID(self, newID):
        self.gameID = newID
