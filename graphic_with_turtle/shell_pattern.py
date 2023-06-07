from turtle import*

pencolor("red")
pensize(2)
fillcolor("green")
speed("slow")
for i in range(10,0,-1):
    begin_fill()
    circle(i*10)
    lt(25)
    end_fill()
mainloop()    