import pygame
from settings import WIDTH, HEIGHT, BLACK, WHITE, WINNING_SCORE, FPS
from paddle import Paddle
from ball import Ball
from scores import save_scores


class Pong:
    def __init__(self, mode):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pong")

        # Création des objets
        self.ball = Ball()
        self.paddle_left = Paddle(20, HEIGHT // 2 - 50)
        self.paddle_right = Paddle(WIDTH - 30, HEIGHT // 2 - 50, is_ai=(mode == "AI"))

        self.running = True
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 50)
        self.score_left = 0
        self.score_right = 0
        self.mode = mode

    def reset(self):
        self.score_left = 0
        self.score_right = 0
        self.ball.reset()
        self.run()

    def draw_text(self, text, x, y):
        """Affiche un texte sur l'écran"""
        text_surface = self.font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        self.show_end_screen()

    def handle_events(self):
        """Gestion des entrées utilisateur"""
        keys = pygame.key.get_pressed()

        # Mouvement des raquettes
        if keys[pygame.K_w]:
            self.paddle_left.move("UP")
        if keys[pygame.K_s]:
            self.paddle_left.move("DOWN")

        if self.mode == "2P":
            if keys[pygame.K_UP]:
                self.paddle_right.move("UP")
            if keys[pygame.K_DOWN]:
                self.paddle_right.move("DOWN")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """Mise à jour des objets"""
        self.ball.move()

        if self.mode == "AI":
            self.paddle_right.ai_move(self.ball)

        # Vérification des collisions avec les raquettes
        if self.ball.rect.colliderect(
            self.paddle_left.rect
        ) or self.ball.rect.colliderect(self.paddle_right.rect):
            self.ball.vx = -self.ball.vx

        # Vérification du score
        if self.ball.rect.left <= 0:
            self.score_right += 1
            self.ball.reset()
        if self.ball.rect.right >= WIDTH:
            self.score_left += 1
            self.ball.reset()

        # Vérification de la victoire
        if self.score_left >= WINNING_SCORE:
            self.running = False
        elif self.score_right >= WINNING_SCORE:
            self.running = False

    def draw(self):
        """Affichage des objets"""
        self.screen.fill(BLACK)
        self.paddle_left.draw(self.screen)
        self.paddle_right.draw(self.screen)
        self.ball.draw(self.screen)

        self.draw_text(str(self.score_left), WIDTH // 4, 20)
        self.draw_text(str(self.score_right), 3 * WIDTH // 4, 20)

        pygame.display.flip()

    def get_user_name(self):
        self.screen.fill(BLACK)
        winner = (
            "Player 1"
            if self.score_left >= WINNING_SCORE
            else "Player 2" if self.mode == "2P" else "AI"
        )
        self.draw_text(f"{winner} a gagné !", WIDTH // 2 - 100, HEIGHT // 3)
        self.draw_text("Insert UserName", WIDTH // 2 - 150, HEIGHT // 3)
        pygame.display.flip()
        if self.mode == "AI":
            return "AI"

        name = ""
        while True:
            self.draw_text(name, WIDTH // 2 - 200, HEIGHT // 2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return name
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif event.key == pygame.K_ESCAPE:
                        return name
                    else:
                        name += event.unicode
            pygame.display.flip()

            self.screen.fill(BLACK)
            self.draw_text(name, WIDTH // 2 - 200, HEIGHT // 2)
            pygame.display.flip()
            return name

    def show_end_screen(self):
        self.screen.fill(BLACK)

        self.draw_text("ESPACE pour rejouer", WIDTH // 2, HEIGHT // 2)
        self.draw_text("ESC pour quitter", WIDTH // 2, HEIGHT // 2 + 50)

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.reset()
                        waiting = False

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
