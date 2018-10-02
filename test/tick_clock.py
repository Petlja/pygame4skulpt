import pygame as pg

pg.init()

cl = pg.time.Clock()
end = False
counter = 0
while not end:
    cl.tick(1)
    print(cl.get_fps())
    counter += 1
    if counter == 100:
        break

pg.quit()
