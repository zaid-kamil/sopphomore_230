import pgzrun

WIDTH = 600
HEIGHT = 400

p1 = Actor('player')
p2 = Actor('player2')
p1.x = 10 # 10px distance from left
p1.y = 200 # 10px distance from top
p2.x = 10
p2.y = 250

def draw():
    screen.clear()
    p1.draw() # draw player on screen
    p2.draw()
    screen.draw.text("Happy new year 2021",(100,200),color='black',fontsize=100)

def update():
    p1.y += 2
    if p1.y > WIDTH:
        p1.y = 0
    p2.y += 3
    if p2.y > WIDTH:
        p2.y = 0
        
pgzrun.go()
