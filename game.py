import numpy as np

class TicTacToe:
    def __init__(self):
        #initial play
        self.board = np.full((3, 3), ' ')  
        # an empty board
        self.current_player = 'X'  
        # X player

    def display_board(self):
        # display now
        print("\nCurrent Board:")
        for row in self.board:
            print("|".join(row))
            print("-" * 5)
        print("\n")

    def player_move(self):
        #update 
        while True:
            try:
                user_move = input(f"Player {self.current_player}, please enter your move (row,col): ")
                print(f"You entered: {user_move}")
                row, col = map(int, user_move.split(","))
                if self.board[row, col] == ' ':  # check whether empty
                    self.board[row, col] = self.current_player
                    break
                else:
                    print("This spot is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column as two numbers separated by a comma (e.g., 1,2).")

    def check_winner(self):
        #check row and coloum
        for i in range(3):
            if all(self.board[i, j] == self.current_player for j in range(3)):
                return True
            if all(self.board[j, i] == self.current_player for j in range(3)):
                return True
        if all(self.board[i, i] == self.current_player for i in range(3)) or \
           all(self.board[i, 2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def check_draw(self):
        #draw check
        return np.all(self.board != ' ')

    def switch_player(self):
        #switch player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        #game play
        print("Welcome to Tic-Tac-Toe!")
        self.display_board()

        while True:
            self.player_move()
            self.display_board()

            # win
            if self.check_winner():
                print(f"Player {self.current_player} wins! Congratulations!")
                break

            # draw
            if self.check_draw():
                print("It's a draw!")
                break

            # next player
            self.switch_player()

# play game
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
