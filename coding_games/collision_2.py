import pgzrun

WIDTH = 500
HEIGHT = 500
GOT_HIT = False

p1 = Actor('player',(400,50))
box = Rect((20,20),(100,100))

def draw():
    screen.clear()
    screen.draw.filled_rect(box,'red')
    p1.draw()

def update():
    # if you want to change value of this variable in the function
    global GOT_HIT # use it like this or you will get error

    if not GOT_HIT:
        box.x += 2          # move the rectangle from left to right
        if keyboard.up :    
            p1.y -=2
        if keyboard.down :
            p1.y +=2
        if box.x > WIDTH:
            box.x = 0
    if p1.colliderect(box):
        GOT_HIT = True
pgzrun.go()
