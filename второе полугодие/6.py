#6
from turtle import *
forward(90)
right(135)
forward(90)
right(135)
forward(90)
right(135)
pu()
for x in range(1,9):
    for y in range(1,10):
        goto(x*30,y*30)
        dot(2)
done()
