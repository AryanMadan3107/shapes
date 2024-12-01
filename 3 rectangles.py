import pgzrun

WIDTH = 800
HEIGHT = 450

def draw():
    screen.fill("blue")
    r = Rect((400,225),(600,350))
    r.center=400,225
    screen.draw.filled_rect(r,"red")
    re = Rect((400,225),(300,175))
    re.center=400,225
    screen.draw.filled_rect(re,"green")
    

pgzrun.go()