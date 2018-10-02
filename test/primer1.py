import pygame as pg

pg.init()
dimenzije_prozora = (200, 200)
prozor = pg.display.set_mode(dimenzije_prozora)
pg.draw.rect(prozor, pg.Color("white"), (50, 50, 100, 100))
pg.display.update()
while pg.event.wait().type != pg.QUIT: pass
pg.quit()
