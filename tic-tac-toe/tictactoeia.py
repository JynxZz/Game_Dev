# Script to create a classic tic tac toe game in the terminal
# RL agent vs Random Move Computer
# Using for to test RL agent on it

# Created by: JynxZz
# Date: 11.05.2024
# Version: 1.0.0

###
# Imports
###
import random


###
# Class
###
class TicTacToeAI:
    def __init__(self):
        self.board = [[None] * 3 for _ in range(3)]
        self.order = ["X", "O"] if random.choice([True, False]) else ["O", "X"]
        self.game_over = False
        self.reward = 0
        self.step = 1

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

    def reset(self):
        self.board = [[None] * 3 for _ in range(3)]
        self.order = ["X", "O"] if random.choice([True, False]) else ["O", "X"]
        self.game_over = False
        self.reward = 0
        self.step = 1

    def make_move(self, player, action=(-1, -1)):
        if player == "X":
            row, col = action
        else:
            row, col = random.randint(0, 2), random.randint(0, 2)
        while self.board[row][col] is not None:
            row, col = random.randint(0, 2), random.randint(0, 2)

        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] is None:
            self.board[row][col] = player
        else:
            if player == "X":
                print("Invalid move, try again.")
                self.make_move("X")

    def check_sides(self, player, action):
        row, col = action
        up, down = row - 1, row + 1
        left, right = col - 1, col + 1
        up_left, up_right = (up, left), (up, right)
        down_left, down_right = (down, left), (down, right)
        coords = [
            (up, col),
            (down, col),
            (row, left),
            (row, right),
            up_left,
            up_right,
            down_left,
            down_right,
        ]
        for coord in coords:
            if (
                0 <= coord[0] < 3
                and 0 <= coord[1] < 3
                and self.board[coord[0]][coord[1]] == player
            ):
                return True
        return False

    def play_step(self, player, action=(-1, -1)):
        # if player == "X":
        #     action = input("Enter row and column: ").split()
        #     action = (int(action[0]) - 1, int(action[1]) - 1)

        # Make player move
        self.make_move(player, action)

        # Check side of the move & give reward
        if self.step > 1:
            side = self.check_sides(player, action)
            if side:
                self.reward += 1
            else:
                self.reward -= 1

        # Check if game is over & give reward
        winner = self.check_winner()
        if winner is not None:
            self.game_over = True
            if winner == "X":
                self.reward += 10
            elif winner == "O":
                self.reward -= 10
            else:
                self.reward += 5

        self.step += 1
        self.order.reverse()

        return action, self.reward, self.game_over


# def play_game():
#     game = TicTacToeAI()
#     while not game.game_over:
#         player = game.order[0]
#         action, reward, done = game.play_step(player)
#         side = game.check_sides(player, action)
#         print(f"Action: {action}")
#         print(f"Reward: {reward}")
#         print(f"Side: {side}")
#         game.draw_board()
#         print("#" * 20)
#     print(game.check_winner())
#     game.draw_board()


# ###
# # Entry point
# ###
# if __name__ == "__main__":
#     play_game()
