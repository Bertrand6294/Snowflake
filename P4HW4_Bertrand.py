#Snowflake
#7/8/19
#P4HW4
#Trevor Bertrand
#

import turtle
import random

#Setup
wn = turtle.Screen()
wn.bgcolor("#EFECCA")
wn.setup(width=250, height=250) 

#Name and colors
turtle = turtle.Turtle()

colors = ["#7D8A2E", "#263248", "#FF8C00", "#F0C600"]

#Start of drawing
def snowflake(size, pensize, x, y):
    """ function that draws a snowflake """
    # turtle.pen(pensize=10)
    turtle.penup()
    turtle.goto(x, y)
    turtle.forward(10*size)
    turtle.left(45)
    turtle.pendown()
    turtle.color(random.choice(colors))

    for i in range(8):
        branch(size)
        turtle.left(45)


#Branches of Snowflake
def branch(size):
    for i in range(3):
        for i in range(3):
            turtle.forward(10.0*size/3)
            turtle.backward(10.0*size/3)
            turtle.right(45)
        turtle.left(90)
        turtle.backward(10.0*size/3)
        turtle.left(45)
    turtle.right(90)
    turtle.forward(10.0*size)

snowflake(8, 6, 0, 0)


