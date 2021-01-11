import pgzrun

WIDTH = 500
HEIGHT = 500

p1 = Actor('player',(400,50))
box = Rect((20,20),(100,100))

def draw():
    screen.clear()
    screen.draw.filled_rect(box,'red')
    p1.draw()

def update():
    box.x += 2
    if p1.colliderect(box):
        print('hit')
pgzrun.go()
