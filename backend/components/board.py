from components.user import User
from components.bot import Bot
import random


class Board:
    def __init__(self, user, isRed):
        self.__columns = 7
        self.__rows = 6
        self.user = user
        self.bot = Bot()
        self.isRed = isRed
        self.board = [[None for i in range(self.__columns)]
                      for j in range(self.__rows)]
        self.available_locations = [(i, j) for i in range(
            self.__rows) for j in range(self.__columns)]
        self.game_finished = False

    def print_board(self):
        for i in range(self.__rows):
            print("\nrow " + str(i) + "  :  ", end="")
            for j in range(self.__columns):
                if self.board[i][j] == None:
                    print("., ", end="")
                else:
                    print(str(self.board[i][j].name) + ", ", end="")
        print()

    def get_available_locations(self):
        avail = {}
        full = False
        for col in range(self.__columns):
            space = False
            for row in range(self.__rows - 1, 0, -1):
                if self.board[row][col] == None:
                    space = True
                    avail.update({str(col): row})
                    break
            if not space:
                avail.update({str(col): None})
        return avail

    def place_piece(self, col_place, row_place):
        # avail = self.get_available_locations()
        # row_place = avail.get(str(col_place))

        # if row_place == -1:
        #     return {
        #         "fine": False,
        #         "user_won": False,
        #         "bot_col": -1,
        #         "bot_row": -1,
        #         "bot_won": False
        #     }
        """""
        # check if position is fine
        if col_place not in range(0, self.__columns - 1):
            return False

        # check if column is not full
        if self.board[0][col_place] != '':
            return False

        # find which row to put in
        for i in range(self.__rows - 1, 0, -1):
            if self.board[i][col_place] == '':
                row_place = i
                break
        """""

        # place column + row
        self.board[row_place][col_place] = self.user

        # call check_won
        won_user = self.check_won(col_place, row_place, self.user)
        if won_user == True:
            print(f"{self.user.name} has won")
            return {
                "fine": True,
                "user_won": True,
                "bot_col": -1,
                "bot_row": -1,
                "bot_won": False
            }

        # call bot
        bot_place = self.bot_placement()
        self.board[bot_place["row"]][bot_place["col"]] = self.bot

        # call check_won
        won_bot = self.check_won(bot_place["col"], bot_place["row"], self.bot)
        if won_bot == True:
            print(f"{self.bot.name} has won")

        # return success, bot (c, r)
        return {
            "fine": True,
            "user_won": False,
            "bot_col": bot_place["col"],
            "bot_row": bot_place["row"],
            "bot_won": won_bot
        }

    def bot_placement(self):
        avail = self.get_available_locations()
        bot_row = avail.get("0")
        move = {
            "col": 0,
            "row": bot_row
        }
        return move

    def check_won(self, position, height, player):
        # Check horizontal
        for i in range(position-3, position+1):
            if i >= 0 and i+3 < self.__columns and all(self.board[height][j] == player for j in range(i, i+4)):
                return True

        # Check vertical
        for i in range(height-3, height+1):
            if i >= 0 and i+3 < self.__rows and all(self.board[j][position] == player for j in range(i, i+4)):
                return True

        # Check diagonal
        for i in range(height-3, height+1):
            for j in range(position-3, position+1):
                if i >= 0 and i+3 < self.__rows and j >= 0 and j+3 < self.__columns:
                    if all(self.board[i+k][j+k] == player for k in range(4)):
                        return True
                    if all(self.board[i+k][j+3-k] == player for k in range(4)):
                        return True
        return False
