import pygame as pg

pg.init()
sat = pg.time.Clock()
kraj = False

counter = 1
while not (kraj):
    for dogadjaj in pg.event.get():
        if dogadjaj == pg.QUIT:
            kraj = True

    sat.tick()
    counter += 1



pg.quit()