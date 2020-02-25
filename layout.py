import pygame
import random
from Python.Projects.Games.Tetris import sprites
#import sprites
from Python.Projects.Games.Tetris import functions
#import functions

pygame.init()
pygame.display.set_caption("Tetris")

screen_width = 620
screen_height = 701

x_grid_cords = [5, 48, 91, 134, 177, 220, 263, 306, 349, 392]
y_grid_cords = [650, 607, 564, 521, 478, 435, 392, 349, 306, 263, 220, 177, 134, 91, 48, 5]

tetris_array = [[0] * 10] * 16

sprite_active = False
# For random sprite
sprite_nr = 0

x = 0
y = 0
vel = 2
rotation = 0

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

    if sprite_active is False:
        sprite_nr = random.randint(1, 6)
        y = -150
        rotation = random.randint(0, 3)

        if sprite_nr == 1:
            from Python.Projects.Games.Tetris.functions import L_x_limits_dict as x_limits_dict
            from Python.Projects.Games.Tetris.functions import L_bot_limits_dict as bot_limits_dict
        if sprite_nr == 2:
            from Python.Projects.Games.Tetris.functions import K_x_limits_dict as x_limits_dict
            from Python.Projects.Games.Tetris.functions import K_bot_limits_dict as bot_limits_dict
        if sprite_nr == 3:
            from Python.Projects.Games.Tetris.functions import S_x_limits_dict as x_limits_dict
            from Python.Projects.Games.Tetris.functions import S_bot_limits_dict as bot_limits_dict
        if sprite_nr == 4:
            from Python.Projects.Games.Tetris.functions import O_x_limits_dict as x_limits_dict
            from Python.Projects.Games.Tetris.functions import O_bot_limits_dict as bot_limits_dict
        if sprite_nr == 5:
            from Python.Projects.Games.Tetris.functions import Z_x_limits_dict as x_limits_dict
            from Python.Projects.Games.Tetris.functions import Z_bot_limits_dict as bot_limits_dict
        if sprite_nr == 6:
            from Python.Projects.Games.Tetris.functions import I_x_limits_dict as x_limits_dict
            from Python.Projects.Games.Tetris.functions import I_bot_limits_dict as bot_limits_dict

        x = x_grid_cords[random.randint(x_limits_dict[rotation][0], x_limits_dict[rotation][1])]
        functions.random_sprite(main_window, x, y, (255, 0, 0), rotation, sprite_nr)
        sprite_active = True

    sprite_active = True
    if y < bot_limits_dict[rotation]:
        y += vel
    functions.random_sprite(main_window, x, y, (255, 0, 0), rotation, sprite_nr)

    if y >= bot_limits_dict[rotation]:
        sprite_active = False

    pygame.display.update()

pygame.quit()
