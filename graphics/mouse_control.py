from turtle import *
import random

def create_flower(x,y):
    penup()
    goto(x,y)
    pendown()
    radius = random.randint(5,30)
    fillcolor('red')
    begin_fill()
    for i in range(6):
        circle(radius)
        left(60)
    end_fill()