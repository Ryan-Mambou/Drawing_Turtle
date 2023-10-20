import random
import random
from turtle import Turtle, Screen

tim = Turtle()

tim.shape('turtle')


def draw_shape(angle, number_of_sides):
    colors = ['blue', 'green', 'yellow', 'red', 'orange', 'indigo', 'pink', 'black', 'brown', 'gray']
    tim.color(random.choice(colors))
    while number_of_sides > 0:
        tim.color(random.choice(colors))
        tim.forward(100)
        tim.right(angle)
        number_of_sides -= 1


for number_of_sides in range(3, 10):
    angle = 360/number_of_sides
    draw_shape(angle, number_of_sides)

screen = Screen()
screen.exitonclick()



