#Andrew Leonard
# threelines.py -> h3-2
#

import turtle
t = turtle.Turtle()
wn = turtle.Screen()
t.pensize(3)
# your picture goes here
#line1
t.left(180)
t.forward(200)

#move to next line
t.right(90)
t.up()
t.forward(30)
t.right(90)
t.down()

#line2
t.forward(200)
t.left(90)

#move to next line
t.up()
t.forward(30)
t.left(90)
t.down()

#line3
t.forward(200)

#return to start
t.left(90)
t.up()
t.forward(60)
t.left(90)
t.forward(200)

#exit
wn.exitonclick()
