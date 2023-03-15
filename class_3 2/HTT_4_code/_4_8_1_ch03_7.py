#
# HTT Ch 4 code example:
#
# Section 4.8: ch03_7
#

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("classic")
tess.hideturtle()
tess.speed(0)

print(list(range(5, 60, 2)))
tess.up()                     # this is new
for size in range(5, 60, 3):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(size)          # move tess along
    tess.right(24)              # and turn her

wn.exitonclick()
