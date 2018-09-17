import pygame as pg

pg.init()
sirina, visina = 400, 400
prozor = pg.display.set_mode([sirina, visina])



kraj = False
prikaz_treba_osveziti = True
boja = "white"
pg.time.set_timer(pg.USEREVENT, 20)
while not kraj:
    pg.time.wait(1000)
    print("ASD")


pg.quit()

