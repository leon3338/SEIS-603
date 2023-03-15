#
# HTT Ch 4 code example:
#
# Section 4.6: colorlist
#

import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(0)
alex.pensize(5)

for aColor in ["green", "red", "purple", "blue"]:
   alex.color(aColor)
   alex.forward(50)
   alex.left(90)

wn.exitonclick()
