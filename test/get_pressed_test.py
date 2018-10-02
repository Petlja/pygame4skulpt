import pygame as pg

pg.init()
sirina, visina = 400, 400
prozor = pg.display.set_mode([sirina, visina])

kraj = False
while not kraj:

    dogadjaj = pg.event.wait()

    if dogadjaj.type == pg.QUIT:
        kraj = True
    pg.key.get_pressed()
    pg.key.get_mods()
    pg.key.set_mods(123)
pg.quit()