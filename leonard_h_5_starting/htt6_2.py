#Andrew Leonard
# htt6_2.py -> h5-3
#
import turtle
def draw_centered_box(turtle,side_length):

    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

wn = turtle.Screen()
andrew = turtle.Turtle()


sz = 20
x_pos = 0
y_pos = 0
n = input("Enter number of boxes: ")
boxes = int(n)

for i in range(boxes):
    draw_centered_box(andrew, sz)
    sz = sz+20
    x_pos = x_pos-10
    y_pos = y_pos-10
    andrew.up()
    andrew.setposition(x_pos,y_pos)
    andrew.down()

andrew.setposition(x_pos,y_pos)
wn.exitonclick()