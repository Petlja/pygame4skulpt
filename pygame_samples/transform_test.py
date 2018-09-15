import pygame as pg

pg.init()

prozor = pg.display.set_mode((400, 400))

font = pg.font.SysFont("arial", 28)
tekst = font.render("asdf", True, pg.Color("yellow"))
prozor.blit(tekst, (0, 0))

pg.display.update()
while True:
    d = pg.event.wait()
    if d.type == pg.KEYDOWN or d.type == pg.KEYUP:
        tekst = pg.transform.flip(tekst, True, False)
        prozor.fill(pg.Color("black"))
        prozor.blit(tekst, (0, 0))
        pg.display.update()
    # pg.time.wait(1000)
