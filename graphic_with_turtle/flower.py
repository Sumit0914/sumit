from turtle import*
import random
s=Screen()
s.setup(500,500)
color=["pink","orange"]
for i in range(50):
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    penup()
    goto(x,y)
    pendown()
    pensize(random.randint(1,2))
    pencolor(color[random.randint(0,1)])
    radius=random.randint(5,30)
    fillcolor("red")
    begin_fill()
    for i in range(6):
        circle(radius)
        left(60)
    end_fill()
mainloop()        
