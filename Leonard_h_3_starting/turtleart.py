#Andrew Leonard
#turtleart.py -> h3-4
#

import random
import turtle

wn = turtle.Screen()
wn.bgcolor("orange")
wn.screensize(1000, 1000)
andrew = turtle.Turtle()

andrew.pensize(10)
andrew.pencolor("green")
andrew.fillcolor("blue")
andrew.shape("turtle")
andrew.begin_fill()
n = input("enter the number of triangles you want: ")
number_steps = int(n)


for i in range(number_steps):

    andrew.left(120)
    andrew.forward(100)
    andrew.right(120)
    andrew.forward(100)
    andrew.right(120)
    andrew.forward(100)

    andrew.up()
    andrew.left(random.randint(0, 359))
    andrew.forward(20)
    andrew.down()

wn.exitonclick()
