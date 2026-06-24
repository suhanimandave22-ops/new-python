import pygame
import random
import sys
from pathlib import Path

pygame.init()

# ==========================
# SETTINGS
# ==========================
WIDTH = 1540
HEIGHT = 790
CELL_SIZE = 20
FPS = 12

BG_COLOR = (25, 25, 35)
GRID_COLOR = (40, 40, 55)

SNAKE_COLOR = (0, 220, 100)
HEAD_COLOR = (0, 255, 140)

FOOD_COLOR = (255, 70, 70)

WHITE = (255, 255, 255)
YELLOW = (255, 220, 50)
RED = (255, 80, 80)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Professional Snake Game")

CLOCK = pygame.time.Clock()

FONT = pygame.font.SysFont("Arial", 28)
BIG_FONT = pygame.font.SysFont("Arial", 60, bold=True)

HIGHSCORE_FILE = Path("highscore.txt")


# ==========================
# HIGH SCORE
# ==========================
def load_highscore():
    try:
        return int(HIGHSCORE_FILE.read_text().strip())
    except:
        return 0


def save_highscore(score):
    HIGHSCORE_FILE.write_text(str(score))


# ==========================
# SNAKE
# ==========================
class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        # Align snake to grid
        start_x = (WIDTH // 2 // CELL_SIZE) * CELL_SIZE
        start_y = (HEIGHT // 2 // CELL_SIZE) * CELL_SIZE

        self.body = [[start_x, start_y]]
        self.direction = (CELL_SIZE, 0)
        self.grow = False

    def move(self):
        head_x, head_y = self.body[-1]
        dx, dy = self.direction

        new_head = [head_x + dx, head_y + dy]

        self.body.append(new_head)

        if not self.grow:
            self.body.pop(0)
        else:
            self.grow = False

    def change_direction(self, new_dir):
        dx, dy = self.direction
        ndx, ndy = new_dir

        # Prevent instant reverse
        if dx == -ndx and dy == -ndy:
            return

        self.direction = new_dir

    def collision(self):
        head = self.body[-1]

        # Wall collision
        if (
            head[0] < 0
            or head[0] >= WIDTH
            or head[1] < 0
            or head[1] >= HEIGHT
        ):
            return True

        # Self collision
        if head in self.body[:-1]:
            return True

        return False

    def draw(self, screen):
        # Body
        for segment in self.body[:-1]:
            pygame.draw.rect(
                screen,
                SNAKE_COLOR,
                (*segment, CELL_SIZE, CELL_SIZE),
                border_radius=5,
            )

        # Head
        pygame.draw.rect(
            screen,
            HEAD_COLOR,
            (*self.body[-1], CELL_SIZE, CELL_SIZE),
            border_radius=6,
        )


# ==========================
# FOOD
# ==========================
class Food:
    def __init__(self):
        self.position = [0, 0]

    def spawn(self, snake_body):
        while True:
            x = random.randrange(0, WIDTH, CELL_SIZE)
            y = random.randrange(0, HEIGHT, CELL_SIZE)

            if [x, y] not in snake_body:
                self.position = [x, y]
                return

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            FOOD_COLOR,
            (
                self.position[0] + CELL_SIZE // 2,
                self.position[1] + CELL_SIZE // 2,
            ),
            CELL_SIZE // 2,
        )


# ==========================
# GAME
# ==========================
class Game:
    def __init__(self):
        self.highscore = load_highscore()
        self.reset()

    def reset(self):
        self.snake = Snake()

        self.food = Food()
        self.food.spawn(self.snake.body)

        self.score = 0
        self.speed = FPS
        self.paused = False

    def draw_grid(self):
        for x in range(0, WIDTH, CELL_SIZE):
            pygame.draw.line(
                SCREEN,
                GRID_COLOR,
                (x, 0),
                (x, HEIGHT),
            )

        for y in range(0, HEIGHT, CELL_SIZE):
            pygame.draw.line(
                SCREEN,
                GRID_COLOR,
                (0, y),
                (WIDTH, y),
            )

    def draw_text(self, text, font, color, x, y):
        SCREEN.blit(font.render(text, True, color), (x, y))

    def start_screen(self):
        while True:
            SCREEN.fill(BG_COLOR)

            title = BIG_FONT.render(
                "SNAKE GAME",
                True,
                YELLOW,
            )

            SCREEN.blit(
                title,
                (
                    WIDTH // 2 - title.get_width() // 2,
                    180,
                ),
            )

            self.draw_text(
                "Press SPACE to Start",
                FONT,
                WHITE,
                WIDTH // 2 - 140,
                320,
            )

            self.draw_text(
                "Arrow Keys = Move",
                FONT,
                WHITE,
                WIDTH // 2 - 120,
                380,
            )

            self.draw_text(
                "P = Pause",
                FONT,
                WHITE,
                WIDTH // 2 - 70,
                430,
            )

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if (
                    event.type == pygame.KEYDOWN
                    and event.key == pygame.K_SPACE
                ):
                    return

    def game_over_screen(self):
        while True:
            SCREEN.fill(BG_COLOR)

            self.draw_text(
                "GAME OVER",
                BIG_FONT,
                RED,
                WIDTH // 2 - 170,
                180,
            )

            self.draw_text(
                f"Score: {self.score}",
                FONT,
                WHITE,
                WIDTH // 2 - 70,
                320,
            )

            self.draw_text(
                f"High Score: {self.highscore}",
                FONT,
                YELLOW,
                WIDTH // 2 - 110,
                370,
            )

            self.draw_text(
                "R = Restart",
                FONT,
                WHITE,
                WIDTH // 2 - 80,
                450,
            )

            self.draw_text(
                "Q = Quit",
                FONT,
                WHITE,
                WIDTH // 2 - 60,
                500,
            )

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_r:
                        self.reset()
                        return

                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

    def run(self):
        self.start_screen()

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        self.snake.change_direction(
                            (-CELL_SIZE, 0)
                        )

                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction(
                            (CELL_SIZE, 0)
                        )

                    elif event.key == pygame.K_UP:
                        self.snake.change_direction(
                            (0, -CELL_SIZE)
                        )

                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction(
                            (0, CELL_SIZE)
                        )

                    elif event.key == pygame.K_p:
                        self.paused = not self.paused

            if not self.paused:

                self.snake.move()

                # FOOD COLLISION
                if self.snake.body[-1] == self.food.position:

                    self.snake.grow = True
                    self.score += 1

                    self.food.spawn(self.snake.body)

                    self.speed = FPS + (self.score // 5)

                    if self.score > self.highscore:
                        self.highscore = self.score
                        save_highscore(self.highscore)

                # GAME OVER
                if self.snake.collision():
                    self.game_over_screen()

            SCREEN.fill(BG_COLOR)

            self.draw_grid()

            self.food.draw(SCREEN)
            self.snake.draw(SCREEN)

            self.draw_text(
                f"Score: {self.score}",
                FONT,
                WHITE,
                15,
                10,
            )

            self.draw_text(
                f"High Score: {self.highscore}",
                FONT,
                YELLOW,
                15,
                45,
            )

            if self.paused:
                pause_text = BIG_FONT.render(
                    "PAUSED",
                    True,
                    WHITE,
                )

                SCREEN.blit(
                    pause_text,
                    (
                        WIDTH // 2 - pause_text.get_width() // 2,
                        HEIGHT // 2 - 40,
                    ),
                )

            pygame.display.flip()

            CLOCK.tick(self.speed)


# ==========================
# MAIN
# ==========================
if __name__ == "__main__":
    Game().run()