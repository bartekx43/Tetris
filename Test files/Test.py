import pygame as py
py.init()

window = py.display.set_mode((500, 800))
py.display.set_caption("Tetris")

x = 100
y = 100
width = 25
height = 25
vel = 1

space_click = False

delay_r = 0
delay_l = 0

run = True
while run:
    py.time.delay(10)
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    keys = py.key.get_pressed()

    if keys[py.K_RIGHT] and x < 500 - width and delay_r == 0 and y < 800 - width:
        x += 50
        delay_r = 20
    if keys[py.K_LEFT] and x > 0 and delay_l == 0 and y < 800 - width:
        x -= 50
        delay_l = 20

    if keys[py.K_SPACE] and space_click is False:
        vel *= 10
        space_click = True

    if y <= 750:
        y += vel
    window.fill((0, 0, 0))

    if delay_l > 0:
        delay_l -= 1
    if delay_r > 0:
        delay_r -= 1

    py.draw.rect(window, (255, 0, 0), (x, y, width, height))
    py.display.update()

py.quit()
