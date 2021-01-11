import pgzrun

HEIGHT = 500
WIDTH = 700

GAME_OVER = False

p1 = Actor('player',(600,250))
e1 = Rect((20,20), (50,50))

def draw():
    screen.clear()
    screen.draw.filled_rect(e1,'green')
    p1.draw()

def update():
    global GAME_OVER

    if not GAME_OVER:
        
        move_player()
        move_enemy()

    if p1.colliderect(e1):
        GAME_OVER = True

# player move logic
def move_player():
    if keyboard.up :
        p1.y -= 3
    if keyboard.down :
        p1.y += 3
    if keyboard.left :
        p1.x -= 3
    if keyboard.right :
        p1.x += 3
    # boundary logic
    if p1.x > WIDTH:
        p1.x =0
    if p1.y > HEIGHT:
        p1.y =0
    if p1.x < 0:
        p1.x = WIDTH
    if p1.y < 0:
        p1.y = HEIGHT

# enemy chase logic
def move_enemy():
    if e1.x < p1.x:
        e1.x +=1
    if e1.x > p1.x:
        e1.x -=1
    if e1.y < p1.y:
        e1.y +=1
    if e1.y > p1.y:
        e1.y -=1   
pgzrun.go()