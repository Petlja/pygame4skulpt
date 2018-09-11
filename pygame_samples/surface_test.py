import pygame as pg

pg.init()

(sirina, visina) = (400, 200)
prozor = pg.display.set_mode((sirina, visina))

font = pg.font.SysFont("consolas", 40)
font.set_underline(False)


poruka = "Zdravo svete!"
tekst1 = font.render(poruka, True, pg.Color("black"))
tekst2 = font.render(poruka, True, pg.Color("yellow"))
tekst2.convert_alpha()
tekst3 = tekst2.copy()
tekst1.blit(tekst3, (0, 0))
tekst1.set_at((1, 1), pg.Color("yellow"))
print(tekst1.get_at((1, 1)))

print("get_rect(): ", tekst1.get_rect(), tekst1.get_bounding_rect())
(sirina_teksta, visina_teksta) = (tekst1.get_width(), tekst1.get_height())
print(sirina_teksta, visina_teksta)
(x, y) = ((sirina - sirina_teksta) / 2, (visina - visina_teksta) / 2)
prozor.blit(tekst1, (x, y))

pg.display.update()
pg.time.set_timer(pg.USEREVENT, 1000 // 50)
while True:
    pg.time.wait(1000)
    print(prozor.scroll(10, 0))
    pg.display.update()
    d = pg.event.wait()
    if d == pg.QUIT:
        break
