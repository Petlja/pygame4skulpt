# -*- acsection: general-init -*-
import pygame as pg

# uključivanje rada biblioteke PyGame
pg.init()

# podešavamo naslov prozora
pg.display.set_caption("Zdravo svete!")
# otvaramo prozor dimenzije 300x300
(sirina, visina) = (600, 600)
prozor = pg.display.set_mode((sirina, visina))
# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

# font kojim će biti prikazan tekst
font = pg.font.SysFont("consolas", 40)
font.set_underline(True)

# poruka koja će se ispisivati
poruka = "Zdravo svete!"
# gradimo sličicu koja predstavlja tu poruku ispisanu crnom bojom
tekst = font.render(poruka, True, pg.Color("black"))

# određujemo veličinu tog teksta (da bismo mogli da ga centriramo)
(sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height())
# položaj određujemo tako da tekst bude centriran
(x, y) = ((sirina - sirina_teksta) / 2, (visina - visina_teksta) / 2)
# prikazujemo sličicu na odgovarajućem mestu na ekranu
prozor.blit(tekst, (x, y))

# -*- acsection: after-main -*-
# ažuriramo prikaz sadržaja ekrana
pg.display.update()

# čekamo da korisnik isključi prozor
while pg.event.wait().type != pg.QUIT:
  pass

# isključivanje rada biblioteke PyGame
pg.quit()

