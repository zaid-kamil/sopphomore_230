from turtle import *
s = Screen()
s.setup(700,600)

def moveleft():
    setheading(180)
    forward(50)
 
def moveright():
    setheading(0)
    forward(50)

def moveup():
    setheading(90)
    forward(50)

def movedown():
    setheading(270)
    forward(50)

listen() # now turtle will check for keyboard click
onkey(moveup,'Up')
onkey(movedown,'Down')
onkey(moveleft,'Left')
onkey(moveright,'Right')

mainloop()


