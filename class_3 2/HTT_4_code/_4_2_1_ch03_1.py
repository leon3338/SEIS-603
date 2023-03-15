#
# HTT Ch 4 code example:
#
# Section 4.2: ch03_1
#

import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
alex = turtle.Turtle()      # create a turtle named alex
alex.pensize(10)
alex.color("red")
alex.forward(150)           # tell alex to move forward by 150 units
alex.left(45)               # turn by 90 degrees
alex.forward(75)            # complete the second side of a rectangle

wn.exitonclick() # ADDED: keeps window visible until mouse click
