import pygame as pg

pg.init()

prozor = pg.display.set_mode((400, 400))

font = pg.font.SysFont("arial", 100)

tekst = font.render("rotzoom", True, pg.Color("yellow"))
w, h = tekst.get_size()
prozor.fill(pg.Color("black"))
prozor.blit(tekst, (0, 0))
pg.display.update()
for i in range(20):
    d = pg.event.wait()
    if d.type == pg.KEYDOWN:
        tekst = pg.transform.rotozoom(tekst, 30, 0.5)
        prozor.fill(pg.Color("black"))
        prozor.blit(tekst, (0, 0))
        pg.display.update()

tekst = font.render("123", True, pg.Color("yellow"))
w, h = tekst.get_size()
prozor.fill(pg.Color("black"))
prozor.blit(tekst, (0, 0))
pg.display.update()
for i in range(20):
    d = pg.event.wait()
    if d.type == pg.KEYDOWN:
        tekst = pg.transform.flip(tekst, True, False)
        prozor.fill(pg.Color("black"))
        prozor.blit(tekst, (0, 0))
        pg.display.update()

tekst = font.render("rot", True, pg.Color("yellow"))
w, h = tekst.get_size()
prozor.fill(pg.Color("black"))
prozor.blit(tekst, (0, 0))
pg.display.update()
for i in range(20):
    d = pg.event.wait()
    if d.type == pg.KEYDOWN:
        tekst = pg.transform.rotate(tekst, -30)
        prozor.fill(pg.Color("black"))
        prozor.blit(tekst, (0, 0))
        pg.display.update()

tekst = font.render("scale", True, pg.Color("yellow"))
w, h = tekst.get_size()
prozor.fill(pg.Color("black"))
prozor.blit(tekst, (0, 0))
pg.display.update()
while True:
    d = pg.event.wait()
    if d.type == pg.KEYDOWN:
        w = int(w * 0.95)
        h = int(h * 0.95)
        tekst = pg.transform.scale(tekst, (w, h))
        prozor.fill(pg.Color("black"))
        prozor.blit(tekst, (0, 0))
        pg.display.update()
