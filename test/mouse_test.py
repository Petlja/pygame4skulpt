import pygame as pg

pg.init()

print(pg.mouse.get_pressed())
print(pg.mouse.get_rel())
print(pg.mouse.get_pos())
pg.mouse.set_pos(1, 2)
pg.mouse.set_pos((1, 2))
pg.mouse.set_visible(True)
print(pg.mouse.get_focused())