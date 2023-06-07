from turtle import*

s = Screen()
s.setup(1000,700)
colors =["red","orange","green","yellow","blue"]
pencolor("black")
pensize(3)
for i in range(15,0,-1):
    penup()
    setpos(0,-20*i)
    pendown()
    fillcolor(colors[i%5])
    begin_fill()
    circle(20*i)
    end_fill()

mainloop()    