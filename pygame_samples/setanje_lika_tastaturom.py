# -*- acsection: general-init -*-
import pygame as pg, random

# uključujemo rad biblioteke PyGame
pg.init()

# podešavamo događaje tastaturom - prvi događaj se generiše nakon
# 50ms, a svaki naredni nakon 25ms
pg.key.set_repeat(50, 25)

# postavljamo naslov prozora
pg.display.set_caption("setanje broda")

# otvaramo prozor dimenzije 400x400 piksela
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
# učitavamo sliku svemirskog broda
brod = pg.image.load('spaceship.png')
# očitavamo dimenzije slike
brod_sirina = brod.get_width()
brod_visina = brod.get_height()

# koordinate centra prozora
(x, y) = (sirina / 2, visina / 2)
# pomeraji po x i y koordinati
(dx, dy) = (10, 10)

pomeraj = {pg.K_LEFT: (-dx, 0),
           pg.K_RIGHT: (dx, 0),
           pg.K_DOWN: (0, dy),
           pg.K_UP: (0, -dy)}

# u prvom koraku je potrebno nacrtati lopticu
treba_crtati = True
kraj = False
while not kraj:
    # ako je potrebno аžurirati sliku
    if treba_crtati:
       # bojimo prozor u belo
       prozor.fill(pg.Color("black"))
       # crtamo svemirski brod
       prozor.blit(brod, (x - brod_sirina / 2, y - brod_visina / 2))
       # ažuriramo prikaz sadržaja prozora
       pg.display.update()
       treba_crtati = False

    # obrađujemo prvi događaj koji se desi
    dogadjaj = pg.event.wait()
    # isključivanje prozora
    if dogadjaj.type == pg.QUIT:
        kraj = True
    # pritisak tastera na tastaturi
    if dogadjaj.type == pg.KEYDOWN:
        if dogadjaj.key in pomeraj:
           # pomeramo centar broda za odgovarajući pomeraj
           (DX, DY) = pomeraj[dogadjaj.key]
           x += DX
           y += DY
           # pošto je brod pomeren, ponovo ćemo crtati scenu
           treba_crtati = True

# -*- acsection: after-main -*-
# isključujemo rad biblioteke PyGame
pg.quit()
