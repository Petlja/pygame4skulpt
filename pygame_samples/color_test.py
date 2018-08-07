import pygame as pg

ccc = pg.Color("pink")
print("ccc", len(ccc))
print(ccc.hsla)
ccc.hsla = (120.0, 100.0, 50.0, 0.0)
print(ccc.r)
print(ccc.g)
print(ccc.b)
print(ccc.a)
h, s, v, a = ccc.hsva

ccc = pg.Color("red")
print(ccc.i1i2i3)
ddd = pg.Color("blue")
ddd.i1i2i3 = (0.3333333333333333, 0.5, -0.25)
print(ddd.r)
print(ddd.g)
print(ddd.b)
print(ccc.normalize())
ccc.a = 100
print(ccc.correct_gamma(0.5))
ccc.set_length(2)
print(len(ccc))
print(ccc.correct_gamma(0.5))
