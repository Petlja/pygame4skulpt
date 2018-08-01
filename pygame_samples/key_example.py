import pygame as pg

pg.init()
prozor = pg.display.set_mode((400, 400))
while True:
    print(pg.key.get_repeat())
    pg.key.set_repeat(20, 50)
    print(pg.key.get_repeat())
    pg.quit()