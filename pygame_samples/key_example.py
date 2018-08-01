import pygame as pg

pg.init()
prozor = pg.display.set_mode((400, 400))
while True:
    pg.time.delay(1000)
    print(pg.key.get_focused())

pg.quit()
