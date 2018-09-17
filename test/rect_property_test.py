import pygame as pg

pg.init()

r = pg.Rect((1, 1), (12, 26))
r.center = (137, 351)
print("2, 2", r.center, r.centerx, r.centery)
r.top = 3
print("top 3", r.top)
r.bottom = 6
print("bottom 6", r.bottom)
r.right = 17
print("right 17", r.right)
r.left = 12
print(r.left)

r.size = (123, 321)
print("size 123321", r.size)

r.w = 888
print("888", r.w, r.width)

r.h = 357
print("357", r.h, r.height)

r.topleft = (0, 0)
print(r.topleft)

r.topright = (0, 1)
print(r.topright)

r.bottomleft = (1, 0)
print(r.bottomleft)

r.bottomright = (1, 1)
print(r.bottomright)

# r = pg.Rect((0, 0), (1, 2))
r.midtop = (1, 0)
print("midtop (1, 0)", r.midtop)
#
r.midbottom = (1, 2)
print("midbottom (1, 2)", r.midbottom)

r.midleft = (3, 1)
print("midleft (3, 1)", r.midleft)

r.midright = (4, 1)
print("midrignt (4, 1)", r.midright)

# print("W=", r.w)
print(r.right)
r.right = 123
print("%d + %d = %d" % (r.left, r.width, r.right))
print("bottom", r.bottom)
r.bottom = 7
print("top, height", r.top, r.height)
r.x = 12
print(r.x)
r.x = r.x + 4
r.left = 3
print(r.x)
r.top = 333123
print(r.y)
print(r.left)
g = r.copy()


print(g.left, g.top, g.width, g.height)
