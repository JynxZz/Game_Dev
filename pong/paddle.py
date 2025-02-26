# Script to create the paddle object
# Author: JynxZz
# Date : 15 Feb 2025

import pygame
from settings import PADDLE_SPEED, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE, HEIGHT, AI_SPEED


class Paddle:
    def __init__(self, x, y, is_ai=False):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED
        self.is_ai = is_ai

    def move(self, direction):
        if direction == "UP" and self.rect.top > 0:
            self.rect.y -= self.speed

        if direction == "DOWN" and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def ai_move(self, ball):
        if self.rect.centery < ball.rect.centery:
            self.rect.y += AI_SPEED
        if self.rect.centery > ball.rect.centery:
            self.rect.y -= AI_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)
