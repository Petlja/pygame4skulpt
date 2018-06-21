import pygame as pg

pg.init()
sirina, visina = 400, 400
prozor = pg.display.set_mode([sirina, visina])

x, y = 200, 200 
r = 50 

kraj= False
prikaz_treba_osveziti = True
pg.time.set_timer(pg.USEREVENT, 20)
while not kraj:
    if prikaz_treba_osveziti:
        prozor.fill(pg.Color("white"))
        pg.draw.circle(prozor, pg.Color("green"), [x, y], r)
        pg.display.update()
        prikaz_treba_osveziti = False

    dogadjaj = pg.event.wait()
    
    if dogadjaj.type == pg.QUIT:
         kraj = True
    elif dogadjaj.type == pg.MOUSEBUTTONDOWN:
        x, y = dogadjaj.pos
        prikaz_treba_osveziti = True
    elif dogadjaj.type == pg.KEYDOWN:
        if dogadjaj.key == pg.K_LEFT:
            x = (x - 50) % sirina
        elif dogadjaj.key == pg.K_RIGHT:
            x = (x + 50) % sirina
        elif dogadjaj.key == pg.K_UP:
            y = (y - 50) % visina
        elif dogadjaj.key == pg.K_DOWN:
            y = (y + 50) % visina
    elif dogadjaj.type == pg.USEREVENT:
        r = (r - 50 + 1) % 100 + 50
        prikaz_treba_osveziti = True

pg.quit()

