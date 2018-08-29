import pygame as pg

pg.init()
sirina, visina = 400, 400
prozor = pg.display.set_mode([sirina, visina])



kraj = False
prikaz_treba_osveziti = True
boja = "white"
pg.time.set_timer(pg.USEREVENT, 20)
while not kraj:
    if prikaz_treba_osveziti:
        prozor.fill(pg.Color(boja))
        pg.display.update()
        prikaz_treba_osveziti = False

    dogadjaj = pg.event.wait()

    if dogadjaj.type == pg.QUIT:
        kraj = True
    elif dogadjaj.type == pg.MOUSEMOTION:
        if dogadjaj.buttons[0] == 1:
            boja = "black"
        prikaz_treba_osveziti = True
    elif dogadjaj.type == pg.MOUSEBUTTONUP:
        boja = "white"
        prikaz_treba_osveziti = True


pg.quit()

