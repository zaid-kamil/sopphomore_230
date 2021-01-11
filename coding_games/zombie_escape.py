import pgzrun
import random
WIDTH = 1000
HEIGHT = 450

soldier = Actor('soldier',center =(50,150))
zombie1 = Actor('zombie',midright =(1320,50))
zombie2 = Actor('zombie',midright =(1000,200))
zombie3 = Actor('zombie',midright =(1550,350))
score = 0
msg = ''
killed = False
def draw():
    screen.clear()
    soldier.draw()
    zombie1.draw()
    zombie2.draw()
    zombie3.draw()
    screen.draw.text(msg,(450,10),color='red',fontsize=32)
def update(d):
    global score,msg,killed
    if not killed:
        zombie1.x -= random.randint(0,10)
        if zombie1.x<0:
            zombie1.x = WIDTH
        zombie2.x -= random.randint(0,10)
        if zombie2.x<0:
            zombie2.x = WIDTH
        zombie3.x -= random.randint(0,10)
        if zombie3.x<0:
            zombie3.x = WIDTH

    if keyboard.UP and soldier.y > 50:
        soldier.y-=5
    if keyboard.DOWN and soldier.y < HEIGHT-50:
        soldier.y+=5
    if soldier.colliderect(zombie1) or soldier.colliderect(zombie2) or soldier.colliderect(zombie3):
        msg = 'GAME OVER'
        killed = True
    elif not killed:
        score +=d
        msg = f'score = {int(score)}'
pgzrun.go()