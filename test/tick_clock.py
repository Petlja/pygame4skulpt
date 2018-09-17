import pygame as pg

pg.init()
sat = pg.time.Clock()
kraj = False

counter = 0

while not (kraj):
    sat.tick(1)
    print(sat.get_fps())

    counter += 1
    if counter == 100:
        break


pg.quit()