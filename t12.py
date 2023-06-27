from turtle import *
from polygon import *

speed ("fastest")

for i in range(5):
    hexagon()   # calling
    for i in range(3):
        triangle()
        for i in range(4):
            square()
            lt(360/4)
        lt(360/3)
    lt(360/5)        

hideturtle()
mainloop()