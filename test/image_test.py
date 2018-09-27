import pygame as pg

pg.init()

(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))

brod = pg.image.load('spaceship.png')
pg.image.save(brod, 'asdf')

