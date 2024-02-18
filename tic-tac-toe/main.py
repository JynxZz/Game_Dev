# Script to create a tic tac toe game using python & pygame
# Using for to test RL agent on it
#
# Created by: JynxZz
# Date: 15.02.2023
# Version: 1.0


###
# Imports
###

import pygame


###
# Variables & setup
###

# Screen
WIDTH, HEIGHT = 800, 800

# Columns & rows for board
SIZE = 9
ROW = 3
COL = 3

# Colors
WHITE, BLACK, RED, GREEN, BLUE = (
    (255, 255, 255),
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
)
GREY = (150, 150, 150)
LIGHT_GREY = (200, 200, 200)
DARK_GREY = (100, 100, 100)

# Setup pygame

game_exit = False

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

###
# Functions
###


def draw_board(col: int = COL, row: int = ROW):
    # draw a gmae board using pygame
    for i in range(1, col):
        pygame.draw.line(
            screen, BLACK, (i * WIDTH / col, 0), (i * WIDTH / col, HEIGHT), 2
        )

    for i in range(1, row):
        pygame.draw.line(
            screen, BLACK, (0, i * HEIGHT / row), (WIDTH, i * HEIGHT / row), 2
        )


###
# Main
###


while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

    screen.fill(WHITE)
