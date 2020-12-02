from turtle import *

pencolor('red')
fillcolor('yellow')
pensize(2)
speed('fastest')
for i in range(25,0,-1):
    begin_fill()
    circle(i*5)
    left(30)
    end_fill()
hideturtle() # hide arrow 
penup()
goto(0,250)
pencolor('green')
write('Assignment: Draw this pattern in turtle',align='center',font=('Arial',18,'bold'))
goto(0,-250)
write('digipodium|Sohpomore',align='center',font=('Arial',12,'bold'))
mainloop()