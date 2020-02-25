import pygame
import random
#from Python.Projects.Games.Tetris import sprites
import sprites
#from Python.Projects.Games.Tetris import functions
import functions

pygame.init()
pygame.display.set_caption("Tetris")

screen_width = 620
screen_height = 701

x_grid_cords = [5, 48, 91, 134, 177, 220, 263, 306, 349, 392]
y_grid_cords = [650, 607, 564, 521, 478, 435, 392, 349, 306, 263, 220, 177, 134, 91, 48, 5]

tetris_array = [[0] * 10] * 16

sprite_active = False
x = 0
y = 0
vel = 1
rotation = 0

main_window = pygame.display.set_mode((screen_width, screen_height))

run = True
while run:
    pygame.time.delay(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    main_window.fill((255, 255, 255))
    pygame.draw.rect(main_window, (105, 105, 105), (5, 5, 433, 691))
    pygame.draw.rect(main_window, (192, 192, 192), (443, 5, 172, 691))

    if sprite_active is False:
        x = x_grid_cords[random.randint(0, 9)]
        y = -150
        rotation = random.randint(0, 3)
        sprites.L_block(main_window, x, y, (255, 0, 0), rotation)
        sprite_active = True

    sprite_active = True
    if y < functions.L_limits_dict[rotation]:
        y += vel
    sprites.L_block(main_window, x, y, (255, 0, 0), rotation)

    pygame.display.update()

pygame.quit()
