# Script to create a tic tac toe game
# Using for to test RL agent on it
#
# Created by: JynxZz
# Date: 15.02.2023
# Version: 1.0


###
# Imports
###

import pygame
import random


###
# Variables & setup
###

# Screen
WIDTH, HEIGHT = 500, 500

# Columns & rows for board
BLOCK_SIZE = 100
ROW = 3
COL = 3

# Colors
COLORS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "grey": (150, 150, 150),
    "light_grey": (200, 200, 200),
    "dark_grey": (100, 100, 100),
}
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (150, 150, 150)
LIGHT_GREY = (200, 200, 200)
DARK_GREY = (100, 100, 100)

# Setup pygame
game_exit = False


###
# Class
###
class TicTacToe:
    def __init__(self, width, height, background):
        self.width = width
        self.height = height
        self.background = background

        # Init display
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tic Tac Toe")
        self.screen.fill(self.background)
        pygame.display.update()

        self.clock = pygame.time.Clock()

        # Draw Board
        self.draw_board()
        self.__calculate_centers()

        # Set turn & winner
        self.turn = 1
        self.winner = False
        self.game_over = False
        self.positions = list()
        self.order = self.__toss()

    # methode to draw the board
    def draw_board(self):
        # vertical lines
        for col in range(1, COL):
            pygame.draw.line(
                self.screen,
                WHITE,
                (BLOCK_SIZE + col * BLOCK_SIZE, BLOCK_SIZE),
                (BLOCK_SIZE + col * BLOCK_SIZE, self.height - BLOCK_SIZE),
                2,
            )

        # horizontal lines
        for row in range(1, ROW):
            pygame.draw.line(
                self.screen,
                WHITE,
                (BLOCK_SIZE, BLOCK_SIZE + row * BLOCK_SIZE),
                (self.width - BLOCK_SIZE, BLOCK_SIZE + row * BLOCK_SIZE),
                2,
            )

        pygame.display.update()

    # method to get the center of box
    def __calculate_centers(self):
        self.board_pos = list()
        self.centers = list()

        for row in range(ROW):
            for col in range(COL):
                box = (
                    BLOCK_SIZE + (BLOCK_SIZE * row),
                    BLOCK_SIZE + (BLOCK_SIZE * col),
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
                self.board_pos.append(box)

        for box in self.board_pos:
            x, y, width, height = box
            center_x = x + width / 2
            center_y = y + height / 2
            self.centers.append((center_x, center_y))

    # methode to get the order
    def __toss(self):
        # Random to choose the first player
        player_1 = "X"
        player_2 = "O"

        order = (player_1, player_2)

        if random.randint(0, 1):
            return order[::-1]
        return order

    # euclidean distance
    def __euclidean_distance(self, point_1, point_2):
        return ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** 0.5

    # find the closest center
    def find_closest_center(self, position):
        min_distance = float("inf")  # Initialise avec une valeur infinie
        closest_index = -1
        for index, center in enumerate(self.centers):
            distance = self.__euclidean_distance(position, center)
            if distance < min_distance:
                min_distance = distance
                closest_index = index
        return self.centers[closest_index], (closest_index + 1)

    def invert_order(self):
        self.order = self.order[::-1]

    def draw_o(self, center):
        radius = BLOCK_SIZE // 3  # Détermine la taille du "O"
        pygame.draw.circle(self.screen, WHITE, center, radius, 2)
        pygame.display.update()

    def draw_x(self, center):
        offset = BLOCK_SIZE // 3  # Détermine la taille du "X"
        # Première ligne (\)
        start_1 = (center[0] - offset, center[1] - offset)
        end_1 = (center[0] + offset, center[1] + offset)
        # Deuxième ligne (/)
        start_2 = (center[0] - offset, center[1] + offset)
        end_2 = (center[0] + offset, center[1] - offset)

        pygame.draw.line(self.screen, WHITE, start_1, end_1, 2)
        pygame.draw.line(self.screen, WHITE, start_2, end_2, 2)
        pygame.display.update()

    def check_winner_inverted_grid(self, game_list):
        # Mapping positions to 'X' or 'O'
        board = {pos: player for pos, player in game_list}

        # Adjusted winning combinations for the inverted grid
        wins = [
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),  # columns
            (1, 4, 7),
            (2, 5, 8),
            (3, 6, 9),  # rows
            (1, 5, 9),
            (3, 5, 7),  # diagonals
        ]

        for win in wins:
            if board.get(win[0]) == board.get(win[1]) == board.get(win[2]) != None:
                self.winner = True
                print(f"Player {board.get(win[0])} wins!")

        return None

    def turn_step(self):
        empty = True

        # Get the center
        center, idx = game.find_closest_center(event.pos)

        # Check position empty
        for tup in self.positions:
            if tup[0] == idx:
                empty = False
                break

        # Draw and next player
        if not self.positions or empty:
            if game.order[0] == "X":
                game.draw_x(center)
                self.positions.append((idx, "X"))
            else:
                game.draw_o(center)
                self.positions.append((idx, "O"))

        print(dict(empty=empty, positions=self.positions, order=self.order[0]))

        # Check if is a winner position
        self.check_winner_inverted_grid(self.positions)
        if len(self.positions) == 9 or self.winner:
            print(self.winner)
            self.game_over = True
            print(self.order[0])

        # Next player
        game.invert_order()


###
# Main
###

if __name__ == "__main__":
    pygame.init()

    game = TicTacToe(WIDTH, HEIGHT, BLACK)

    # Game Loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.turn_step()

        if game.game_over:
            print("Game Over")
            game.screen.fill(BLACK)
            game.draw_board()
            game.positions = list()
            game.game_over = False

        if game_exit:
            break

    pygame.quit()
