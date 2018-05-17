import turtle
import pygame
import math
import time
pygame.init()
s = pygame.Surface([300, 300])
print("sirina ", s.get_width())
print("visina ", s.get_height())
print("proba")
print(s)
screen = pygame.display.set_mode([400, 400])
print(screen)
print(screen.get_width())

c = pygame.Color(1, 2, 3, 4)
c.r = 5
print(c)

r = pygame.Rect((10, 300), (80, 20))
print(r)
r.top = 19
print(r)
r = pygame.draw.rect(screen, pygame.Color('brown'), r)
print(r)

r = pygame.draw.line(screen, (255, 0, 0, 255) , [10, 10], [550, 50], 3)
print(r)
c = pygame.Color('blue')
print(c)
pygame.draw.line(screen, c, [150, 10], [550, 50])

pygame.draw.lines(screen, (0, 0, 255, 1), True, [[0, 80], [50, 90], [200, 80], [220, 30]])

r = pygame.draw.lines(screen, pygame.Color('navyblue'), True, [[300, 300], [310, 350], [350, 350]], 0)
print(r)

r = pygame.draw.polygon(screen, pygame.Color('lightsalmon2'), [[100, 300], [150, 320], [180, 300], [140, 250]])
print("poligon r: ", r)

r = pygame.draw.circle(screen, pygame.Color('red'), [200, 200], 50)
print("krug r:", r)

r.width = 200
r = pygame.draw.arc(screen, pygame.Color('green'), r, 0, math.pi / 3, 10)
print("arc r: ", r)

r = pygame.draw.ellipse(screen, pygame.Color('blue'), r, 2);
print("elipe r: ", r)

pygame.draw.aaline(screen, c, [150, 200], [350, 200])

e = pygame.event.Event(5,{"key":22})
print(e)
print(e.key)

done = False
is_blue = True
x = 30
y = 30

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("gotova petlja")
            done = True
        if event.type == pygame.KEYDOWN:
            print("otkucano: "+ str(event.key))
    time.sleep(1)

print("A sada malo kornjace")
wn = turtle.Screen()

babbage = turtle.Turtle()
babbage.shape("triangle")

n = 8
angle = 360/n

for i in range(n):
    babbage.right(angle)
    babbage.forward(90)
    babbage.stamp()

wn.exitonclick()