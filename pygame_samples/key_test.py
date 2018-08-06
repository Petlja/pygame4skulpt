import pygame as pg

pg.init()
pg.display.set_mode((800, 600))


print([pg.key.name(i) for i in range(323)])
pg.key.get_mods()
pg.key.set_mods()
pg.key.get_focused()
pg.key.get_pressed()
pg.key.get_repeat()
pg.key.set_repeat()

