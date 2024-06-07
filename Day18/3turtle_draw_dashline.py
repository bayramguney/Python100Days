# https://docs.python.org/3/library/turtle.html
# https://trinket.io/docs/colors
# https://cs111.wellesley.edu/reference/colors
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()
