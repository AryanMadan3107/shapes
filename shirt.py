import pgzrun
import random

WIDTH=600
HEIGHT=600

w=WIDTH
h=150
red=random.randint(0,255)
green=random.randint(0,255)
blue=random.randint(0,255)

def draw():
    w=WIDTH
    h=150
    screen.fill((red,green,blue))
    for i in range(50):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        re = Rect((0,300),(w,h))
        re.center = 300,300
        screen.draw.rect(re,(r,g,b) )
        h+=10
        w-=10
    screen.draw.text("Hi!",center=(300,300),color="blue")
pgzrun.go()