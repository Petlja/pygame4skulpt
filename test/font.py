import pygame as pg

pg.init()

(sirina, visina) = (600, 600)
prozor = pg.display.set_mode((sirina, visina))

prozor.fill(pg.Color("white"))

font = pg.font.SysFont("consolas", 40)
font.set_underline(True)

poruka = "Zdravo svete!"
tekst = font.render(poruka, True, pg.Color("yellow"))

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

