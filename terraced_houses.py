from turtle import *
import time

pencolor('hotpink')
pensize(5)
for i in range(3):
    # point turtle in the right direction
    # so the triangle points upward
    left(60)
    forward(100)
    time.sleep(0.5)
    # draw the triangle
    for i in range(2):
        right(120)
        forward(100)
        time.sleep(0.5)
    # draw the square (three sides)
    for i in range(3):
        left(90)
        forward(100)
        time.sleep(0.5)
    # make turtle point to right
    # before repeat for another house
    right(90)
    
