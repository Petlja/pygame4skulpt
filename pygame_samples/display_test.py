import pygame as pg

pg.init()
print(pg.display.get_init())
pg.display.init()
print(pg.display.get_init())
pg.display.set_mode((400, 400))
pg.display.set_caption("cap cap")
print(pg.display.get_caption())
