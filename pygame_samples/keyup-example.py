import pygame as pg

pg.init()
sirina, visina = 400, 400
prozor = pg.display.set_mode([sirina, visina])



kraj = False
prikaz_treba_osveziti = True
crno = True
pg.time.set_timer(pg.USEREVENT, 20)
while not kraj:
    if prikaz_treba_osveziti:
        if crno:
            prozor.fill(pg.Color("black"))
        else:
            prozor.fill(pg.Color("white"))
        pg.display.update()
        prikaz_treba_osveziti = False

    dogadjaj = pg.event.wait()

    if dogadjaj.type == pg.QUIT:
        kraj = True
    elif dogadjaj.type == pg.KEYDOWN:
        # print("down")
        if not crno:
            crno = True
            prikaz_treba_osveziti = True
    elif dogadjaj.type == pg.KEYUP:
        # print("UP")
        if crno:
            crno = False
            prikaz_treba_osveziti = True

pg.quit()

