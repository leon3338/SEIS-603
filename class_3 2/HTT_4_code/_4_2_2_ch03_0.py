#
# Extra HTT4 code example:
#


import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window

alex = turtle.Turtle()      # create a turtle named alex
alex.forward(100)           # tell alex to move forward by 150 units
alex.left(45)               # turn by 90 degrees
alex.forward(50)            # complete the second side of a rectangle

wn.exitonclick() # ADDED: keeps window visible until mouse click

