from components.user import User


class UserManager:
    def __init__(self):
        self.__list_users = []

    def check_existing(self, to_check):
        # if to_check in self.__list_users:
        #     return True
        # return False
        for user in self.__list_users:
            if user.name == to_check:
                return True
        return False

    def add_new_user(self, to_add):
        if not self.check_existing(to_add):
            self.__list_users.append(User(to_add))
            return True
        else:
            return False

    def find_user(self, to_find):
        for user in self.__list_users:
            if user.name == to_find:
                return user

    def print_users(self):
        for user in self.__list_users:
            print(user.name)

    def get_all_users_in_game(self):
        in_game = []
        for user in self.__list_users:
            if user.gameID != None:
                in_game.append(user)
        return in_game
