# Script to start the game
# Author: JynxZz
# Date : 15 Feb 2025

from game import Pong
from menu import Menu

if __name__ == "__main__":
    while True:
        menu = Menu()
        mode = menu.display()

        game = Pong(mode)
        game.run()
