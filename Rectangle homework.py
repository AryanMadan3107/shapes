import pgzrun

WIDTH=500
HEIGHT=500

def draw():
    r=Rect((0,0),(200,200))
    screen.draw.filled_rect(r,"blue")
    re=Rect((300,300),(200,200))
    screen.draw.rect(re,"blue")
    screen.draw.text("Hello!",center=(100,220),color="blue")
    screen.draw.text("Hi!",center=(400,280),color="blue")

pgzrun.go()