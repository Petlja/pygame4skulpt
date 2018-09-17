import pygame as pg

pg.init()

prozor = pg.display.set_mode((400, 400))

font = pg.font.SysFont("arial", 100)

tekst = font.render("1234567", True, pg.Color("yellow"))
w, h = tekst.get_size()
prozor.fill(pg.Color("black"))
prozor.blit(tekst, (0, 0))
pg.display.update()
cnt = 0
for i in range(10):
    d = pg.event.wait()
    if d.type == pg.KEYDOWN:
        tekst = font.render("1234567", True, pg.Color("yellow"))
        w, h = tekst.get_size()
        tekst = pg.transform.chop(tekst, pg.Rect(w/2 * (cnt % 2), w / 2 * (cnt % 4 / 2), w/2, h/2))
        cnt += 1
        prozor.fill(pg.Color("black"))
        prozor.blit(tekst, (0, 0))
        pg.display.update()

