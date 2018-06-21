import pygame as pg
pg.init()
prozor = pg.display.set_mode([400, 400])
x, y = 50, 50
faza = 0
boje = ["red","green","yellow"]
kraj = False
while not kraj:
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            kraj = True
        elif dogadjaj.type == pg.MOUSEBUTTONDOWN:
            faza = (faza + 1) % 3
    
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, pg.Color(boje[faza]), [x, y], 30)
    pg.display.update()
    pg.time.wait(20)
pg.quit()