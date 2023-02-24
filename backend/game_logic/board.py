import random


class Board:
    def __init__(self, player_one, player_two):
        self.__columns = 7
        self.__rows = 6
        self.__players = [player_one, player_two]
        self.current_turn = random.randint(0, 1)
        self.board = [['' for i in range(self.__columns)]
                      for j in range(self.__rows)]
        self.game_finished = False

    def get_players(self):
        return [self.__players[0].name, self.__players[1].name]

    def print_board(self):
        for i in range(self.__rows):
            print("row", i, self.board[i])
        print()

    def place_piece(self, row_place):
        pass

    def check_won(self, position, height):
        player = self.__players[self.current_turn].get_name()
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
