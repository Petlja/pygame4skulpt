import pygame as pg

pg.init()
try:
    raise pg.error("ASD")
except RuntimeError:
    print("RTE")

print(pg.get_sdl_version())
print(pg.get_sdl_byteorder())
