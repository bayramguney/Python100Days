# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/reference/colors
from turtle import Turtle,Screen
import another_module

print(another_module.another_variable)     # 12
print("#############")

timmy = Turtle()   # constructing from Turtle class  timmy is object
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvheight)  # canvheight is attribute
print(my_screen.canvwidth)
my_screen.exitonclick()




