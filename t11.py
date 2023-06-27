from turtle import *
# defining
def hexagon():
    for i in range(6):
        fd(100)
        lt(72)

def pentagon():
    for i in range(5):
        fd(100)
        lt(72)

for i in range(5):
    hexagon() #calling
    pentagon()
    lt(10)

hideturtle()
mainloop()    


