import pygame as pg
pg.init()

print(pg.font.get_fonts())
print(pg.font.get_default_font())
print(pg.font.match_font('arial'))
print(pg.font.match_font('nonexistentrandomfont'))

# pg.font.Font("asdf", 10)
fnt = pg.font.SysFont("asdf", 10)
fnt.render("check the font size", True, pg.Color("black"))
fnt.set_bold(True)
fnt.set_underline(True)
fnt.set_italic(True)
print(fnt.get_bold())
print(fnt.get_underline())
print(fnt.get_italic())

print(fnt.metrics("asdf"))
