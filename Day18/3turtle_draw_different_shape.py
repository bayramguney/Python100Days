# https://docs.python.org/3/library/turtle.html
# https://trinket.io/docs/colors
# https://cs111.wellesley.edu/reference/colors
import random
from turtle import Turtle, Screen

tim = Turtle()

num_sides = 5
colors = ["red","blue","green","purple"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,10):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)






screen = Screen()
screen.exitonclick()
