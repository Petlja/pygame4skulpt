import pygame as pg

pg.init()

r = pg.Rect((1, 1), (2, 2))
print("<rect(18, 32, 2, 2)>", r.move(17, 31))
print(r)
r.move_ip(17, 31)
print(r)

r = pg.Rect((0, 0), (4, 4))
print(r.inflate(3, 3))
r.inflate_ip(3, 3)
print(r)

clamper = pg.Rect((0, 0), (200, 200))
r = pg.Rect((-10, -10), (5, 5))

print("0, 0, 5, 5)", r.clamp(clamper))
r.clamp_ip(clamper)
print(r)

a = pg.Rect((0, 0), (4, 4))
b = pg.Rect((10, 10), (12, 12))
print("0, 0, 22, 22", a.union(b))
b.union_ip(a)
print(b)

x = pg.Rect(-10, -10, 1, 1)
l = [pg.Rect((i, i), (1, 1)) for i in range(10)]
print("-10, -10, 20, 20", x.unionall(l))
x.unionall_ip(l)
print(x)

a = pg.Rect((1, 2), (3, 4))
b = pg.Rect((5, 6), (7, 8))
print("1, 2, 3, 3", b.fit(a))
upsidedown = pg.Rect((3, 3), (-10, -10))
print(upsidedown.left)
print(upsidedown.right)
upsidedown.normalize()
print(upsidedown.left)
print(upsidedown.right)
print("true?", upsidedown.contains(pg.Rect((0, 0), (1, 1))))


