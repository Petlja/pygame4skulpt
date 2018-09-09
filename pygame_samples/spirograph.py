import math
import pygame as pg


pg.init()

pg.display.set_caption("Spirograph")
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))

(cx, cy) = (sirina // 2, visina // 2)
R = min(sirina//2, visina//2)
k = 0.67
l = 0.67
r = round(k * R)
alpha = 0

kriva = pg.Surface((sirina, visina))
kriva.fill(pg.Color("white"))

pg.time.set_timer(pg.USEREVENT, 1000 // 50)

kraj = False
treba_crtati = True
while not kraj:
    if treba_crtati:
        prozor.fill(pg.Color("white"))
        prozor.blit(kriva, (0, 0))
        pg.draw.circle(prozor, pg.Color("black"), (cx, cy), R, 3)
        pg.draw.circle(prozor, pg.Color("red"), (round(cx + R * math.cos(alpha)), round(cy - R * math.sin(alpha))), 5)
        (mx, my) = (round(cx + (R-r)*math.cos(alpha)), round(cy - (R-r)*math.sin(alpha)))
        pg.draw.circle(prozor, pg.Color("blue"), (mx, my), r, 3)
        beta = - (R - r)/r*alpha
        (Ax, Ay) = (round(mx + l*r*math.cos(beta)), round(my - l*r*math.sin(beta)))
        pg.draw.circle(prozor, pg.Color("red"), (Ax, Ay), 5)

        hue = round(((alpha + math.pi) % (2*math.pi)) / (2*math.pi) * 360)
        boja = pg.Color("black")
        boja.hsva = (hue, 100, 100, 1)
        pg.draw.circle(kriva, boja, (Ax, Ay), 2)
        
        pg.display.update()
        treba_crtati = False
    dogadjaj = pg.event.wait()
    if dogadjaj.type == pg.QUIT:
        kraj = True
    elif dogadjaj.type == pg.USEREVENT:
        alpha += math.pi / 90
        treba_crtati = True
    elif dogadjaj.type == pg.MOUSEMOTION:
        (x, y) = dogadjaj.pos
        phi0 = (alpha + math.pi) % (2*math.pi) - math.pi
        phi = math.atan2(cy - y, x - cx)
        d_phi = phi - phi0
        if d_phi > math.pi:
            d_phi -= 2*math.pi
        if d_phi < -math.pi:
            d_phi += 2*math.pi
        alpha += d_phi
        treba_crtati = True
        
pg.quit()
