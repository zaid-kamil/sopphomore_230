
from turtle import *
bgcolor('black')
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(260):
    pencolor(colors[x % 6]) # x = 1
    width(x / 100 + 1)
    forward(x) # 0
    left(59) # rotate 59
mainloop()