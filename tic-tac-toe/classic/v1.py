# Script to create a classic tic tac toe game in the terminal
# Human vs Computer
# Using for to test RL agent on it
#
# Created by: JynxZz
# Date: 01.04.2024
# Version: 1.1.0


###
# Imports
###
import random


###
# Class
###
class TicTacToe:
    def __init__(self):
        self.board: list = [[None for _ in range(3)] for _ in range(3)]
        self.order = self.__toss()
        self.game_over = False
        self.winner = None

    def check_board(self):
        winner = self.__check_rows(self.board)
        if winner is None:
            winner = self.__check_columns(self.board)
            if winner is None:
                winner = self.__check_diagonals(self.board)
                if winner is None:
                    if self.__is_board_full(self.board):
                        return "Tie"
                    else:
                        return None
        return winner

    def __check_rows(self, board):
        for row in board:
            if set(row) == {"X"}:
                return "X"
            elif set(row) == {"O"}:
                return "O"
        return None

    def __check_columns(self, board):
        columns = [[board[row][col] for row in range(3)] for col in range(3)]
        for column in columns:
            if set(column) == {"X"}:
                return "X"
            elif set(column) == {"O"}:
                return "O"
        return None

    def __check_diagonals(self, board):
        diagonals = [
            [board[i][i] for i in range(3)],
            [board[i][2 - i] for i in range(3)],
        ]
        for diagonal in diagonals:
            if set(diagonal) == {"X"}:
                return "X"
            elif set(diagonal) == {"O"}:
                return "O"
        return None

    def __is_board_full(self, board):
        for row in board:
            if None in row:
                return False
        return True

    def __toss(self):
        return ["X", "O"] if random.randint(0, 1) == 0 else ["O", "X"]

    def __change_order(self):
        return self.order[::-1]

    def __valid_move(self, row, col):
        try:
            self.board[row]
        except IndexError:
            return False
        try:
            self.board[row][col]
        except IndexError:
            return False
        if self.board[row][col] == None:
            return True

    def draw_board(self):
        pipe = " | "
        dash = "- - - - - -"
        for row in range(3):
            print(" " + pipe.join([cell or " " for cell in self.board[row]]))
            if row < 2:
                print(dash)

    def human_move(self):
        row = int(input("Enter row: ")) - 1
        col = int(input("Enter column: ")) - 1

        if self.__valid_move(row, col):
            self.board[row][col] = "X"
        else:
            print("Invalid move")
            self.human_move()

    def computer_move(self):
        while True:
            row, col = random.randint(0, 2), random.randint(0, 2)
            if self.__valid_move(row, col):
                self.board[row][col] = "O"
                break

    def step(self):
        while not self.game_over:
            self.winner = self.check_board()
            self.draw_board()

            if not self.winner:
                if self.order[0] == "X":
                    self.human_move()
                    self.computer_move()
                    self.__change_order()
                else:
                    self.computer_move()
                    self.human_move()
                    self.__change_order()
            else:
                self.game_over = True
                print(f"{self.winner} wins!")
                break


###
# Entry Point
###
if __name__ == "__main__":
    tictactoe = TicTacToe()
    tictactoe.step()
