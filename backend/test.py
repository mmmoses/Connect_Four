from components.board import Board
from components.user import User
from components.user_manager import UserManager

"""""
a = Board(User("A"), True)

a.place_piece(1)
a.print_board()
a.place_piece(2)
a.print_board()
a.place_piece(1)
a.print_board()
a.place_piece(1)
a.print_board()

print(a.bot_placement())
"""""

a = UserManager()
a.add_new_user("a")
a.add_new_user("b")
a.print_users()
print(a.add_new_user("a"))
# print(a.check_existing("a"))
