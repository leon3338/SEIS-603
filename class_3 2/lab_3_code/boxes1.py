#
# L3-4 - boxes1.py:
#
# Draw two nested boxes as shown in handout:
#   Inner box of side 80, centered at origin (turtle's home)
#   Outer box of side 100, also centered at origin
#   (Note this implies horizontal and vertical distance of 10 between squares
#
import turtle as t

wn = t.Screen() # capital letter indicates a CLASS

moxie = t.Turtle()
moxie.speed(0)

#
# draw nested boxes here
#

# move to midpoint of right side of inner square of side 80

# draw inner box

# move to midpoint of right side of outer square of side 100

# draw outer box

# the following waits for click on window, then closes and quits

wn.exitonclick()

