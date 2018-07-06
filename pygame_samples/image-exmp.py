# -*- acsection: general-init -*-
import pygame as pg, math  

# ukljucivanje rada biblioteke PyGame
pg.init()  
    
# podesavamo naslov prozora
pg.display.set_caption("Cat")

# otvaramo prozor dimenzije 300x300
(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

# ucitavamo slicicu iz datoteke cat.png
slika = pg.image.load("cat.png").convert()
#slika = pg.image.load("cat.png")
# prikazujemo slicicu na sredini ekrana
(x, y) = ((sirina - slika.get_width()) / 2, (visina - slika.get_height()) / 2)
prozor.blit(slika, (x, y))

# -*- acsection: after-main -*-
pg.display.update()

# petlja obrade dogadjaja - cekamo dok korisnik ne iskljuci prozor
while pg.event.wait().type != pg.QUIT:
    pass

# iskljucivanje rada biblioteke PyGame
pg.quit()