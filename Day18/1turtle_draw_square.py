# https://docs.python.org/3/library/turtle.html
# https://trinket.io/docs/colors
# https://cs111.wellesley.edu/reference/colors
# https://www.w3schools.com/colors/colors_rgb.asp
from turtle import Turtle


tim = Turtle()
tim.shape("turtle")
tim.color("red")
for _ in range(4):
    tim.forward(100)
    tim.right(90)



