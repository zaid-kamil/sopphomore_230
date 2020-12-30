import pgzrun

WIDTH = 500
HEIGHT = 500

box = Rect((20,20),(50,50))

def draw():
    screen.clear()
    screen.draw.circle((250,250), 50, "white")
    screen.draw.filled_circle((250,100),50,'red')
    screen.draw.line((10,10),(490,490),'purple')
    screen.draw.line((150,20),(350,20),'yellow')
    screen.draw.text("Game 1",(10,480),color='green')
    screen.draw.filled_rect(box, 'red')

def update():
    box.x = box.x + 1 
    if box.x > WIDTH:
        box.x = 0
pgzrun.go()