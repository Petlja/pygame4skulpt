import pygame
for k in dir(pygame):
    v = pygame.__dict__[k]
    if isinstance(v,int):
        vstr = str(v)
    elif isinstance(v,str):
        vstr = "'" + v + "'"
    else:
        vstr = False
    if vstr:
        print("'" + k + "': " + vstr + ",")
    
