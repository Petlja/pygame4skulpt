import pygame as pg

prozor_sirina, prozor_visina = 400, 300 
vx, vy = 40, 20 # piksela u sekundi
stranica = 50 
boja = pg.Color('yellow')
pozadina = pg.Color('black')

pg.init()
prozor = pg.display.set_mode([prozor_sirina, prozor_visina])
while not pg.event.get(pg.QUIT):
    t = pg.time.get_ticks() / 1000 # sekundi od inicijalizacije
    x = (t * vx) % (prozor_sirina - stranica)
    y = (t * vy) % (prozor_visina - stranica)
    prozor.fill(pozadina)
    pg.draw.rect(prozor, boja, pg.Rect(x, y, stranica, stranica))
    pg.display.update()
    pg.time.wait(50)
pg.quit()