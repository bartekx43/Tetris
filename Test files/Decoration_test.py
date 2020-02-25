import pygame as py
py.init()

window = py.display.set_mode((500, 500))

run = True
while run:
    py.time.delay(10)
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    py.draw.rect(window, (255, 0, 0), (15, 15, 470, 470))
    py.display.update()

py.quit()
