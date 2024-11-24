import pgzrun

WIDTH=800
HEIGHT=450

def draw():
    screen.fill("red")
    r = Rect((0,225),(800,225))
    r.center = 400,225
    screen.draw.rect(r, "green")
pgzrun.go()