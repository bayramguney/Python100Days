# https://docs.python.org/3/library/turtle.html
# https://trinket.io/docs/colors
# https://cs111.wellesley.edu/reference/colors
import random
import turtle
from turtle import Turtle, Screen

my_tuple = (1,2,3)
print(my_tuple[2])
# my_tuple[2] = 5        TUPLES are immutable it can not be changed.

tim = Turtle()
turtle.colormode(255)   # from package not from object
tim.shape("turtle")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
directions = [0,90,180,270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))



screen = Screen()
screen.exitonclick()
