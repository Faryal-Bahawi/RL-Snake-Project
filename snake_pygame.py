import pygame
import sys
import random
import os

# ---------- Game Settings ----------
WIDTH, HEIGHT = 600, 600      # Window size (pixels)
CELL_SIZE = 20                # Size of one grid cell
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE

SNAKE_SPEED = 12              # Frames per second (higher = smoother)

# Colors
BLACK  = (0, 0, 0)
WHITE  = (255, 255, 255)
GREEN  = (0, 200, 0)
GREEN_DARK = (0, 120, 0)
GREEN_LIGHT = (100, 255, 100)
RED    = (230, 40, 40)
GRAY   = (40, 40, 40)
YELLOW = (255, 215, 0)

HIGH_SCORE_FILE = "highscore.txt"

# ---------- Helper Functions ----------

def random_food_position(snake):
    """Return a random (x, y) cell not occupied by the snake."""
    while True:
        x = random.randint(0, COLS - 1)
        y = random.randint(0, ROWS - 1)
        if [x, y] not in snake:
            return [x, y]

def draw_grid(surface):
    # Very subtle grid for a smoother look
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(surface, (25, 25, 25), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, (25, 25, 25), (0, y), (WIDTH, y))

def draw_snake(surface, snake):
    for i, (x, y) in enumerate(snake):
        px = x * CELL_SIZE
        py = y * CELL_SIZE
        rect = pygame.Rect(px, py, CELL_SIZE, CELL_SIZE)

        # Outer darker body (border)
        pygame.draw.rect(surface, GREEN_DARK, rect, border_radius=6)

        # Inner lighter "skin"
        inner = rect.inflate(-6, -6)
        pygame.draw.rect(surface, GREEN_LIGHT, inner, border_radius=8)

        if i == 0:
            # Head overlay
            head_inner = rect.inflate(-4, -4)
            pygame.draw.rect(surface, GREEN, head_inner, border_radius=10)

            # Eyes
            eye_radius = 2
            eye_offset_x = CELL_SIZE // 4
            eye_offset_y = CELL_SIZE // 4

            pygame.draw.circle(
                surface,
                WHITE,
                (px + CELL_SIZE - eye_offset_x, py + eye_offset_y),
                eye_radius
            )
            pygame.draw.circle(
                surface,
                WHITE,
                (px + CELL_SIZE - eye_offset_x, py + CELL_SIZE - eye_offset_y),
                eye_radius
            )

def draw_food(surface, food):
    x, y = food
    px = x * CELL_SIZE
    py = y * CELL_SIZE
    rect = pygame.Rect(px, py, CELL_SIZE, CELL_SIZE)

    # Slightly rounded red square
    pygame.draw.rect(surface, RED, rect, border_radius=8)

    # Little highlight
    highlight = rect.inflate(-10, -10)
    pygame.draw.rect(surface, (255, 120, 120), highlight, border_radius=10)

def show_text(surface, text, size, color, center, bold=True):
    font = pygame.font.SysFont("arial", size, bold=bold)
    render = font.render(text, True, color)
    rect = render.get_rect(center=center)
    surface.blit(render, rect)

def load_sound(name):
    """Try to load a sound. If file not found, return None (silent mode)."""
    path = os.path.join(os.path.dirname(__file__), name)
    if not os.path.exists(path):
        return None
    try:
        return pygame.mixer.Sound(path)
    except Exception:
        return None

def load_high_score():
    if not os.path.exists(HIGH_SCORE_FILE):
        return 0
    try:
        with open(HIGH_SCORE_FILE, "r") as f:
            return int(f.read().strip() or 0)
    except Exception:
        return 0

def save_high_score(score):
    try:
        current = load_high_score()
        if score > current:
            with open(HIGH_SCORE_FILE, "w") as f:
                f.write(str(score))
    except Exception:
        pass

# ---------- Simple "AI Brain" ----------

def choose_ai_direction(snake, food, current_direction):
    """
    Very simple AI:
    - Tries all 4 directions
    - Ignores moves that hit wall or self
    - Among safe moves, picks one that gets closer to the food
    """
    head_x, head_y = snake[0]
    fx, fy = food

    # All possible directions: up, down, left, right
    candidates = [
        [0, -1],  # up
        [0, 1],   # down
        [-1, 0],  # left
        [1, 0],   # right
    ]

    # Don't allow 180° turn (reverse)
    opposite = [-current_direction[0], -current_direction[1]]

    best_move = None
    best_dist = None

    for move in candidates:
        if move == opposite:
            continue  # skip direct reverse to avoid instant self-hit

        nx = head_x + move[0]
        ny = head_y + move[1]

        # Check if out of bounds
        if nx < 0 or nx >= COLS or ny < 0 or ny >= ROWS:
            continue

        # Check collision with body
        if [nx, ny] in snake:
            continue

        # Manhattan distance to food
        dist = abs(nx - fx) + abs(ny - fy)

        if best_move is None or dist < best_dist:
            best_move = move
            best_dist = dist

    # If no safe "smart" move found, try any safe move
    if best_move is None:
        safe_moves = []
        for move in candidates:
            if move == opposite:
                continue
            nx = head_x + move[0]
            ny = head_y + move[1]
            if (
                0 <= nx < COLS and
                0 <= ny < ROWS and
                [nx, ny] not in snake
            ):
                safe_moves.append(move)
        if safe_moves:
            best_move = random.choice(safe_moves)
        else:
            best_move = current_direction  # completely stuck, just keep going

    return best_move

# ---------- Main Game Loop ----------

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake RL Game")
    clock = pygame.time.Clock()

    # Sounds (optional – game works even if files are missing)
    eat_sound = load_sound("eat_drink.wav")
    game_over_sound = load_sound("game_over.wav")

    # Game states: "MENU", "PLAYING", "GAME_OVER"
    state = "MENU"

    score = 0
    high_score = load_high_score()

    # control_mode: "HUMAN" or "AI"
    control_mode = "HUMAN"

    # Snake + game variables (will be reset when starting game)
    snake = []
    direction = [1, 0]
    food = [0, 0]

    def reset_game():
        nonlocal snake, direction, food, score
        head_x = COLS // 2
        head_y = ROWS // 2
        snake = [
            [head_x, head_y],
            [head_x - 1, head_y],
            [head_x - 2, head_y],
        ]
        direction = [1, 0]  # moving right
        food = random_food_position(snake)
        score = 0

    reset_game()

    running = True
    while running:
        # ----- Events -----
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                # Toggle control mode with C key
                if event.key == pygame.K_c:
                    control_mode = "AI" if control_mode == "HUMAN" else "HUMAN"

                if state == "MENU":
                    if event.key == pygame.K_SPACE:
                        state = "PLAYING"

                elif state == "PLAYING" and control_mode == "HUMAN":
                    # Movement controls (no 180° turn)
                    if event.key in (pygame.K_UP, pygame.K_w) and direction != [0, 1]:
                        direction = [0, -1]
                    elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != [0, -1]:
                        direction = [0, 1]
                    elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != [1, 0]:
                        direction = [-1, 0]
                    elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != [-1, 0]:
                        direction = [1, 0]

                elif state == "GAME_OVER":
                    if event.key == pygame.K_SPACE:
                        reset_game()
                        state = "PLAYING"
                    elif event.key == pygame.K_m:
                        reset_game()
                        state = "MENU"

        # ----- Update -----
        if state == "PLAYING":
            # If AI mode, choose direction automatically each frame
            if control_mode == "AI":
                direction = choose_ai_direction(snake, food, direction)

            head_x, head_y = snake[0]
            new_head = [head_x + direction[0], head_y + direction[1]]

            # Check collision with walls or self
            if (
                new_head[0] < 0 or new_head[0] >= COLS or
                new_head[1] < 0 or new_head[1] >= ROWS or
                new_head in snake
            ):
                state = "GAME_OVER"
                save_high_score(score)
                high_score = load_high_score()
                if game_over_sound is not None:
                    game_over_sound.play()
            else:
                snake.insert(0, new_head)

                # Check food
                if new_head == food:
                    score += 1
                    if eat_sound is not None:
                        eat_sound.play()
                    food = random_food_position(snake)
                else:
                    snake.pop()

        # ----- Draw -----
        screen.fill(BLACK)

        if state == "MENU":
            show_text(screen, "SNAKE RL", 54, GREEN_LIGHT, (WIDTH // 2, HEIGHT // 2 - 80))
            show_text(screen, "Use ARROWS or WASD to move", 24, WHITE, (WIDTH // 2, HEIGHT // 2))
            show_text(screen, "Press SPACE to start", 24, YELLOW, (WIDTH // 2, HEIGHT // 2 + 40))
            show_text(screen, "Press C to toggle HUMAN / AI", 22, WHITE, (WIDTH // 2, HEIGHT // 2 + 80))
            show_text(screen, f"High Score: {high_score}", 24, GREEN_LIGHT, (WIDTH // 2, HEIGHT // 2 + 120))

        elif state in ("PLAYING", "GAME_OVER"):
            # Background grid + snake + food
            draw_grid(screen)
            draw_snake(screen, snake)
            draw_food(screen, food)

            # Top bar for score, high score, mode
            pygame.draw.rect(screen, (15, 15, 15), (0, 0, WIDTH, 40))
            show_text(screen, f"Score: {score}", 22, WHITE, (80, 20), bold=True)
            show_text(screen, f"High: {high_score}", 22, YELLOW, (WIDTH - 80, 20), bold=True)
            show_text(screen, f"Mode: {control_mode}", 20, WHITE, (WIDTH // 2, 20), bold=True)

            if state == "GAME_OVER":
                # Dark overlay
                overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 160))
                screen.blit(overlay, (0, 0))

                show_text(screen, "GAME OVER", 48, RED, (WIDTH // 2, HEIGHT // 2 - 40))
                show_text(screen, f"Final Score: {score}", 28, WHITE, (WIDTH // 2, HEIGHT // 2))
                show_text(screen, "SPACE = Restart   M = Menu", 22, YELLOW, (WIDTH // 2, HEIGHT // 2 + 40))

        pygame.display.flip()
        clock.tick(SNAKE_SPEED)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
