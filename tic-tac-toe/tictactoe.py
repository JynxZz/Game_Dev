# Script to create a classic tic tac toe game in the terminal
# Human vs Computer
# Using for to test RL agent on it
#
# Created by: JynxZz
# Date: 01.04.2024
# Version: 1.2.0

###
# Imports
###
import random


###
# Class
###
class TicTacToe:
    def __init__(self):
        self.board = [[None] * 3 for _ in range(3)]
        self.order = ["X", "O"] if random.choice([True, False]) else ["O", "X"]
        self.game_over = False

    def check_winner(self):
        lines = (
            self.board  # Rows
            + list(zip(*self.board))  # Columns
            + [
                [self.board[i][i] for i in range(3)],  # Diagonal
                [self.board[i][2 - i] for i in range(3)],  # Anti-diagonal
            ]
        )
        for line in lines:
            if len(set(line)) == 1 and line[0] is not None:
                return line[0]
        if all(cell is not None for row in self.board for cell in row):
            return "Tie"
        return None

    def draw_board(self):
        pipe = " | "
        line_separator = "- - - - - -"
        for i, row in enumerate(self.board):
            print(pipe.join([cell if cell is not None else " " for cell in row]))
            if i < 2:
                print(line_separator)

    def make_move(self, player):

        if player == "X":  # Human
            self.draw_board()
            row, col = map(int, input("Enter row and column: ").split())
            row -= 1
            col -= 1
        else:  # Computer
            row, col = random.randint(0, 2), random.randint(0, 2)
            while self.board[row][col] is not None:
                row, col = random.randint(0, 2), random.randint(0, 2)

        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] is None:
            self.board[row][col] = player
        else:
            if player == "X":
                print("Invalid move, try again.")
                self.make_move("X")

    def play_game(self):

        while not self.game_over:
            winner = self.check_winner()

            if winner:
                print("#" * 20)
                print("Final board:")
                self.draw_board()
                self.game_over = True
                print(f"{winner} wins!" if winner != "Tie" else "It's a tie!")
                break

            self.make_move(self.order[0])
            self.order.reverse()

    def reset(self):
        self.board = [[None] * 3 for _ in range(3)]
        self.order = ["X", "O"] if random.choice([True, False]) else ["O", "X"]
        self.game_over = False


###
# Entry Point
###
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
