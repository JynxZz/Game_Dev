# Script to create the menu
# Author: JynxZz
# Date : 15 Feb 2025

import pygame
from settings import WIDTH, HEIGHT, WHITE, BLACK


class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.Font(None, 35)

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def display(self):
        running = True
        mode = None

        while running:
            self.screen.fill(BLACK)
            self.draw_text("PONG", WIDTH // 2, HEIGHT // 4)
            self.draw_text("Press 1 for Singleplayer", WIDTH // 2, HEIGHT // 2)
            self.draw_text("Press 2 for Multiplayer", WIDTH // 2, HEIGHT // 2 + 50)
            self.draw_text("Press Q to Quit", WIDTH // 2, HEIGHT // 2 + 100)

            self.draw_text("Best :", WIDTH // 2, HEIGHT // 2 + 150)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        mode = "AI"
                        running = False
                    if event.key == pygame.K_2:
                        mode = "2P"
                        running = False
                    if event.key == pygame.K_q:
                        running = False

        return mode
