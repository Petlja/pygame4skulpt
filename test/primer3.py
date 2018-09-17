import pygame as pg

pg.init()
prozor = pg.display.set_mode([400, 400])

x, y = 200, 200 
r = 50 

kraj = False
while not kraj:
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, pg.Color("green"), [x, y], r)
    pg.display.update()

    dogadjaj = pg.event.wait()
    if dogadjaj.type == pg.QUIT:
         kraj = True
    elif dogadjaj.type == pg.MOUSEBUTTONDOWN:
        x, y = dogadjaj.pos

pg.quit()