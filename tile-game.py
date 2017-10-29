import pygame
import random

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
GRID_SQUARE_SIZE = 50
GRID_HEIGHT = int((WINDOW_HEIGHT / GRID_SQUARE_SIZE) - 1)
GRID_WIDTH = int((WINDOW_WIDTH / GRID_SQUARE_SIZE) - 1)
GRID_DESIGN = ["##########",
               "#        #",
               "# #    # #",
               "#        #",
               "#        #",
               "#        #",
               "#        #",
               "# #    # #",
               "#        #",
               "##########"]
SCORE = 0


def is_tile_walkable(x_test, y_test):
    return True if GRID_DESIGN[y_test][x_test] == ' ' or GRID_DESIGN[y_test][x_test] == 'T' else False


def is_tile_this(x_test, y_test, test_tile):
    return True if GRID_DESIGN[y_test][x_test] == test_tile else False


def change_tile(x_pos, y_pos, new_tile):
    lst_row = list(GRID_DESIGN[y_pos])
    lst_row[x_pos] = new_tile
    GRID_DESIGN[y_pos] = ''.join(lst_row)


def gen_target():
    global grid_pos
    target_x, target_y = random.randint(0, 9), random.randint(0, 9)
    while not is_tile_walkable(target_x, target_y) and not is_tile_this(target_x, target_y, 'T') and (target_x, target_y) != grid_pos:
        target_x, target_y = random.randint(0, 9), random.randint(0, 9)
    change_tile(target_x, target_y, 'T')
    print("Target created at ({}, {})".format(target_x, target_y))


def change_targets(old_grid_pos, new_grid_pos):
    global SCORE
    # if old pos was T then it must be emptied and score updated
    if is_tile_this(old_grid_pos[0], old_grid_pos[1], 'T'):
        change_tile(old_grid_pos[0], old_grid_pos[1], ' ')
        SCORE += 1
        gen_target()


def update_grid_pos(old_grid_pos):
    new_grid_x, new_grid_y = old_grid_pos
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if is_tile_walkable(new_grid_x, new_grid_y - 1):
            new_grid_y -= 1
    if pressed[pygame.K_DOWN]:
        if is_tile_walkable(new_grid_x, new_grid_y + 1):
            new_grid_y += 1
    if pressed[pygame.K_LEFT]:
        if is_tile_walkable(new_grid_x - 1, new_grid_y):
            new_grid_x -= 1
    if pressed[pygame.K_RIGHT]:
        if is_tile_walkable(new_grid_x + 1, new_grid_y):
            new_grid_x += 1
    new_grid_x = min(GRID_WIDTH, max(new_grid_x, 0))
    new_grid_y = min(GRID_HEIGHT, max(new_grid_y, 0))
    new_grid_pos = (new_grid_x, new_grid_y)

    change_targets(old_grid_pos, new_grid_pos)
    return new_grid_pos


def update_movement(screen_pos, grid_pos):
    screen_x, screen_y = screen_pos
    if screen_x < grid_pos[0] * GRID_SQUARE_SIZE:
        screen_x += 2
    elif screen_x > grid_pos[0] * GRID_SQUARE_SIZE:
        screen_x -= 2
    if screen_y < grid_pos[1] * GRID_SQUARE_SIZE:
        screen_y += 2
    elif screen_y > grid_pos[1] * GRID_SQUARE_SIZE:
        screen_y -= 2
    return min(WINDOW_WIDTH - GRID_SQUARE_SIZE, max(0, screen_x)), \
           min(WINDOW_HEIGHT - GRID_SQUARE_SIZE, max(0, screen_y))


def draw_game():
    screen.fill((0, 0, 0))
    for y, row in enumerate(GRID_DESIGN):
        for x, tile in enumerate(row):
            if tile == '#':
                pygame.draw.rect(screen, wall_color,
                                 pygame.Rect(x * GRID_SQUARE_SIZE, y * GRID_SQUARE_SIZE, GRID_SQUARE_SIZE,
                                             GRID_SQUARE_SIZE))
            elif tile == ' ':
                pygame.draw.rect(screen, empty_color,
                                 pygame.Rect(x * GRID_SQUARE_SIZE, y * GRID_SQUARE_SIZE, GRID_SQUARE_SIZE,
                                             GRID_SQUARE_SIZE))
            elif tile == 'T':
                pygame.draw.rect(screen, target_color,
                                 pygame.Rect(x * GRID_SQUARE_SIZE, y * GRID_SQUARE_SIZE, GRID_SQUARE_SIZE,
                                             GRID_SQUARE_SIZE))
            elif tile == 'P':
                # player should be stored server side so will not be in map variable
                pass
    # this draws the player (moving or not)
    pygame.draw.rect(screen, player_color, pygame.Rect(pos[0], pos[1], GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))
    # draw score
    score_text = FONT.render("Score - {0}".format(SCORE), 1, (255, 255, 255))
    screen.blit(score_text, (10, 5))


pygame.init()
FONT = pygame.font.Font('amatic/Amatic-Bold.ttf', 32)
screen = pygame.display.set_mode(WINDOW_SIZE)
done = False
pos = (50, 50)
FPS = 60
grid_pos = (1, 1)
player_color = (255, 255, 255)
empty_color = (0, 0, 0)
wall_color = (0, 0, 200)
target_color = (200, 0, 0)
clock = pygame.time.Clock()

gen_target()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # INPUT
    if tuple([i * GRID_SQUARE_SIZE for i in grid_pos]) == pos:
        grid_pos = update_grid_pos(grid_pos)
    pos = update_movement(pos, grid_pos)

    # DRAW
    draw_game()

    # UPDATE
    pygame.display.flip()
    clock.tick(FPS)
