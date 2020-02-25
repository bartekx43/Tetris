import pygame
#from Python.Projects.Games.Tetris import sprites
import sprites

pygame.init()
pygame.display.set_caption("Tetris")

screen_width = 620
screen_height = 800

main_window = pygame.display.set_mode((screen_width, screen_height))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    main_window.fill((255, 255, 255))
    pygame.draw.rect(main_window, (105, 105, 105), (5, 5, 433, 790))
    pygame.draw.rect(main_window, (192, 192, 192), (443, 5, 172, 790))

    sprites.building_block(main_window, 100, 100, (255, 0, 0))
    sprites.L_block(main_window, 150, 150, (255, 120, 50), 0)
    sprites.K_block(main_window, 150, 300, (255, 120, 50), 2)

    pygame.display.update()

pygame.quit()
