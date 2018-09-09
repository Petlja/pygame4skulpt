import pygame as pg

pg.init()

(sirina, visina) = (400, 200)
prozor = pg.display.set_mode((sirina, visina))

font = pg.font.SysFont("consolas", 40)
font.set_underline(False)

poruka = "Zdravo svete!"
tekst1 = font.render(poruka, True, pg.Color("black"))
tekst2 = font.render(poruka, True, pg.Color("yellow"))
# tekst1.blit(tekst2, (0, 0))

(sirina_teksta, visina_teksta) = (tekst1.get_width(), tekst1.get_height())
print(sirina_teksta, visina_teksta)
(x, y) = ((sirina - sirina_teksta) / 2, (visina - visina_teksta) / 2)
prozor.blit(tekst1, (x, y))

pg.display.update()

while True:
    d = pg.event.wait()
    if d == pg.QUIT:
        break
