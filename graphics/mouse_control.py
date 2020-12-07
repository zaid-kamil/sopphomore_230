from turtle import *
import random

speed('fastest')
s = Screen()
s.setup(700,700)

fillcolor('red')
def create_flower(x,y):
    penup()
    goto(x,y)
    pendown()
    radius = random.randint(5,30)
    begin_fill()
    for i in range(6):
        circle(radius)
        left(60)
    end_fill()
s.onclick(create_flower)
mainloop()