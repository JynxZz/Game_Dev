# A simple Tic Tac Toe game
# This game supports basic Tic Tac Toe functionality with a graphical interface,
# allowing two players to take turns marking spaces on a 3x3 grid.

# Author: JynxZz
# Date: 31.03.2024
# Version: 1.1 (Refactored for clarity and modularity)

# Imports
import pygame
import random

# Screen dimensions
WIDTH, HEIGHT = 500, 500
BLOCK_SIZE = 100  # Size of each block in the grid

# Color definitions
COLORS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
}


class TicTacToe:
    def __init__(self):
        """Initialize the game, setting up the display and game state."""
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tic Tac Toe")
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        """Reset the game state for a new game."""
        self.screen.fill(COLORS["black"])
        self.positions = [None] * 9  # Represents a 3x3 grid
        self.order = self.decide_order()
        self.game_over = False
        self.winner = None
        self.draw_board()

    def decide_order(self):
        """Randomly decide the order of players for the game."""
        return ["X", "O"] if random.randint(0, 1) == 0 else ["O", "X"]

    def draw_board(self):
        """Draw the Tic Tac Toe board on the screen."""
        for col in range(1, 3):
            pygame.draw.line(
                self.screen,
                COLORS["white"],
                (col * BLOCK_SIZE, 0),
                (col * BLOCK_SIZE, HEIGHT),
                2,
            )
        for row in range(1, 3):
            pygame.draw.line(
                self.screen,
                COLORS["white"],
                (0, row * BLOCK_SIZE),
                (WIDTH, row * BLOCK_SIZE),
                2,
            )
        pygame.display.update()

    def draw_mark(self, pos, mark):
        """Draw an X or O mark on the board at the specified position."""
        row, col = divmod(pos, 3)
        center = ((col + 0.5) * BLOCK_SIZE, (row + 0.5) * BLOCK_SIZE)
        if mark == "X":
            self.draw_x(center)
        else:
            self.draw_o(center)
        self.positions[pos] = mark
        self.check_winner()

    def draw_x(self, center):
        """Draw an X at the specified center position."""
        offset = BLOCK_SIZE // 3
        pygame.draw.line(
            self.screen,
            COLORS["white"],
            (center[0] - offset, center[1] - offset),
            (center[0] + offset, center[1] + offset),
            2,
        )
        pygame.draw.line(
            self.screen,
            COLORS["white"],
            (center[0] - offset, center[1] + offset),
            (center[0] + offset, center[1] - offset),
            2,
        )
        pygame.display.update()

    def draw_o(self, center):
        """Draw an O at the specified center position."""
        pygame.draw.circle(self.screen, COLORS["white"], center, BLOCK_SIZE // 3, 2)
        pygame.display.update()

    def check_winner(self):
        """Check the board for a winning combination and update the game state."""
        wins = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),  # Rows
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),  # Columns
            (0, 4, 8),
            (2, 4, 6),  # Diagonals
        ]
        for win in wins:
            if (
                self.positions[win[0]]
                == self.positions[win[1]]
                == self.positions[win[2]]
                and self.positions[win[0]] is not None
            ):
                self.winner = self.positions[win[0]]
                self.game_over = True
                return

        if all(pos is not None for pos in self.positions):
            self.game_over = True  # Draw

    def handle_click(self, position):
        """Handle a mouse click event by placing a mark or resetting the game."""
        if self.game_over:
            self.reset()
            return

        col = position[0] // BLOCK_SIZE
        row = position[1] // BLOCK_SIZE
        pos = row * 3 + col

        if self.positions[pos] is None:
            self.draw_mark(pos, self.order[0])
            self.order = self.order[::-1]  # Swap player turn

    def run(self):
        """Main game loop to process events and update the screen."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()
