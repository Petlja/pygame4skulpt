import math, random
import pygame as pg

pg.init()

pg.display.set_caption("krugovi na dijagonali")
(sirina, visina) = (400, 500)
prozor = pg.display.set_mode((sirina, visina))


def nasumicna_boja():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def crtaj():
    r = d / (2 * n)
    kx = sirina / (2 * n)
    ky = visina / (2 * n)
    prozor.fill(pg.Color("white"))
    for i in range(n):
        (cx, cy) = ((2 * i + 1) * kx, visina - (2 * i + 1) * ky)
        pg.draw.circle(prozor, nasumicna_boja(), (round(cx), round(cy)), round(r), 2)
    pg.display.update()


d = math.sqrt(sirina ** 2 + visina ** 2)

n = 5
crtaj()

kraj = False
while not kraj:
    dogadjaj = pg.event.wait()
    if dogadjaj.type == pg.QUIT:
        kraj = True
    elif dogadjaj.type == pg.MOUSEBUTTONDOWN:
        if dogadjaj.button == 1:
            n += 1
            crtaj()
        elif dogadjaj.button == 3 and n > 1:
            n -= 1
            crtaj()
    if dogadjaj.type == pg.KEYDOWN:
        if dogadjaj.key == pg.K_UP:
            n += 1
            crtaj()
        elif dogadjaj.key == pg.K_DOWN and n > 1:
            n -= 1
            crtaj()

pg.quit()
