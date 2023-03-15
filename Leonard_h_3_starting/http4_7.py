#Andrew Leonard
# http4_7.py -> h3-3
#
import random
import turtle

wn = turtle.Screen()
andrew = turtle.Turtle()

n = input("enter the number of steps: ")
number_steps = int(n)

for i in range(number_steps):
    andrew.left(random.randint(0, 359))
    andrew.forward(100)


print("The pirate's final heading was", andrew.heading(), "and location", andrew.xcor(), andrew.ycor())

wn.exitonclick()
