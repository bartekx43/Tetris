# IMPORTS
# ------------------------------------------------------------------------
import pygame
import random
from Python.Projects.Games.Tetris import sprites
#import sprites
from Python.Projects.Games.Tetris import functions
#import functions
from functools import partial


pygame.init()
pygame.display.set_caption("Tetris")

# AUDIO
# --------------------------------------------------------------------------
song = pygame.mixer.music.load('pymusic.mp3')
pygame.mixer.music.play(-1)

# GLOBAL VARIABLES
# --------------------------------------------------------------------------
screen_width = 620
screen_height = 701

x_grid_cords = [5, 48, 91, 134, 177, 220, 263, 306, 349, 392]
y_grid_cords = [5, 48, 91, 134, 177, 220, 263, 306, 349, 392, 435, 478, 521, 564, 607, 650]

x_limits_dict_dict = {
    1: functions.L_x_limits_dict,
    2: functions.K_x_limits_dict,
    3: functions.S_x_limits_dict,
    4: functions.O_x_limits_dict,
    5: functions.Z_x_limits_dict,
    6: functions.I_x_limits_dict
}

movement_dict_dict = {
    1: functions.L_dict,
    2: functions.K_dict,
    3: functions.S_dict,
    4: functions.O_dict,
    5: functions.Z_dict,
    6: functions.I_dict
}

# BEGINNING INITIALIZATIONS
# -------------------------------------------------------------------------
sprite_status = "Dead"
sprite_nr = 0
x = 0
y = 0
vel = 1
rotation = 0
color = (0, 0, 0)
movement_dict = functions.L_dict
x_limits_dict = functions.L_x_limits_dict
delay_r = 0
delay_l = 0
delay_rot = 0
delay_dropped = 0
y_limit_array = [650, 650, 650, 650, 650, 650, 650, 650, 650, 650]
color_array = [[(0, 0, 0)] * 16 for _ in range(10)]
coord_array = [[(0, 0)] * 16 for _ in range(10)]
space_click = False


# RUNNING WINDOW
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
main_window = pygame.display.set_mode((screen_width, screen_height))

run = True
while run:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    main_window.fill((255, 255, 255))
    pygame.draw.rect(main_window, (105, 105, 105), (5, 5, 433, 691))
    pygame.draw.rect(main_window, (192, 192, 192), (443, 5, 172, 691))

    if sprite_status == "Dead":
        # Defining parameters
        sprite_nr = random.randint(1, 6)
        y = -150
        rotation = random.randint(0, 3)
        color = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
        delay_dropped = 100

        x_limits_dict = x_limits_dict_dict[sprite_nr]
        movement_dict = movement_dict_dict[sprite_nr]

        x = x_grid_cords[random.randint(x_limits_dict[rotation][0], x_limits_dict[rotation][1])]
        sprite_status = "Falling"

    function_dict = {
        1: partial(sprites.L_block, main_window, x, y, color, rotation),
        2: partial(sprites.K_block, main_window, x, y, color, rotation),
        3: partial(sprites.S_block, main_window, x, y, color, rotation),
        4: partial(sprites.O_block, main_window, x, y, color, rotation),
        5: partial(sprites.Z_block, main_window, x, y, color, rotation),
        6: partial(sprites.I_block, main_window, x, y, color, rotation)
    }

    if not(functions.is_ok(x, y + vel, movement_dict[rotation], coord_array, x_grid_cords, y_grid_cords)):
        vel = 1

    if functions.is_ok(x, y, movement_dict[rotation], coord_array, x_grid_cords, y_grid_cords):
        sprite_status = "Falling"
        delay_dropped = 100
        y += vel
        vel = 1

    function_dict[sprite_nr]()

    if not (functions.is_ok(x, y, movement_dict[rotation], coord_array, x_grid_cords, y_grid_cords)):

        if sprite_status == "Falling":
            sprite_status = "Dropped"

        if delay_dropped == 0:
            sprite_status = "Dead"
        else:
            delay_dropped -= 1

        # Setting color of block
        # -------------------------------------
        if sprite_status == "Dead":
            x_cord = x_grid_cords.index(x)
            y_cord = y_grid_cords.index(y)
            color_array[x_cord][y_cord] = color
            functions.set_array(x_cord, y_cord, color, color_array, movement_dict[rotation], y_limit_array)
            functions.update_array(x, y, movement_dict[rotation], y_limit_array, x_grid_cords)
            functions.coordinate_array(coord_array, color_array, x_grid_cords, y_grid_cords)

    # CONTROLS
    # --------------

    keys = pygame.key.get_pressed()

    key_right_condition1 = keys[pygame.K_RIGHT] and x < x_grid_cords[x_limits_dict[rotation][1]] and delay_r == 0
    key_right_condition2 = functions.is_ok(x + 43, y, movement_dict[rotation], coord_array, x_grid_cords, y_grid_cords)
    key_right_condition3 = keys[pygame.K_RIGHT] and (sprite_status == "Dropped") and functions.is_ok_x(x + 43, y, movement_dict[rotation], coord_array, x_grid_cords, y_grid_cords) and delay_r == 0

    if key_right_condition1 and key_right_condition2 or key_right_condition3:
        x += 43
        delay_r = 20

    key_left_condition1 = keys[pygame.K_LEFT] and delay_l == 0 and (functions.is_ok(x - 43, y, movement_dict[rotation], coord_array, x_grid_cords, y_grid_cords))
    key_left_condition2 = keys[pygame.K_LEFT] and (sprite_status == "Dropped") and functions.is_ok_x(x - 43, y, movement_dict[rotation], coord_array, x_grid_cords, y_grid_cords) and delay_l == 0

    if key_left_condition1 or key_left_condition2:
        x -= 43
        delay_l = 20

    if keys[pygame.K_r] and delay_rot == 0 and functions.is_ok(x, y, movement_dict[(rotation+1) % 4], coord_array, x_grid_cords, y_grid_cords):
        rotation += 1
        rotation %= 4
        delay_rot = 35
    if keys[pygame.K_SPACE]:
        vel = 10

    if delay_l > 0:
        delay_l -= 1
    if delay_r > 0:
        delay_r -= 1
    if delay_rot > 0:
        delay_rot -= 1

# DELETING FULL ROWS
# --------------------------

    color_array = functions.delete_full_rows(color_array)
    functions.coordinate_array(coord_array, color_array, x_grid_cords, y_grid_cords)

# DISPLAYING DEAD BLOCKS
# -------------------------------------------------------------
    for i, row in enumerate(color_array):
        for j, column in enumerate(row):
            if column != (0, 0, 0):
                sprites.building_block(main_window, x_grid_cords[i], y_grid_cords[j], color_array[i][j])

    pygame.display.update()

pygame.quit()
