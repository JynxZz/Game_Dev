# Script to create the ball object
# Author: JynxZz
# Date : 15 Feb 2025

import pygame
import random
from settings import BALL_SIZE, BALL_SPEED, WHITE, WIDTH, HEIGHT


class Ball:
    def __init__(
        self,
    ):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
        self.vx = BALL_SPEED * random.choice([-1, 1])
        self.vy = BALL_SPEED * random.choice([-1, 1])

    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        # Checking collisions
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.vy = -self.vy

    def reset(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
        self.vx = BALL_SPEED * random.choice([-1, 1])
        self.vy = BALL_SPEED * random.choice([-1, 1])

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)
