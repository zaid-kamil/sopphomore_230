import pgzrun

WIDTH = 600
HEIGHT = 400

bg = Actor('bg1',topleft=(0,0))
p1 = Actor('player',midleft=(0,250))
p2 = Actor('player2',midright=(600,350))
cloud1 = Actor('cloud',topleft=(100,30))
cloud2 = Actor('cloud2',topleft=(0,10))

def draw():
    screen.clear()
    bg.draw()
    cloud1.draw()
    cloud2.draw()
    p1.draw()
    p2.draw()

def update():
    if keyboard.right:
        p1.x += 2
    if keyboard.left:
        p1.x -= 2
    if keyboard.D:
        p2.x += 2
    if keyboard.A:
        p2.x -= 2
    
    cloud1.x += 2
    if cloud1.x > WIDTH:
        cloud1.x =0
    cloud2.x += 1
    if cloud2.x > WIDTH:
        cloud2.x =0

pgzrun.go()