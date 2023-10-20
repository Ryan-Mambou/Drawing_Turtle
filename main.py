import random
import random
from turtle import Turtle, Screen

tim = Turtle()

tim.shape('turtle')

colors = ['dark goldenrod', 'pale turquoise', 'light coral', 'indigo', 'medium violet red', 'hot pink', 'pale violet',
          'tomato', 'goldenrod', 'dark cyan']


def draw_shape(angle, number_of_sides):
    while number_of_sides > 0:
        tim.forward(100)
        tim.right(angle)
        number_of_sides -= 1


for number_of_sides in range(3, 10):
    angle = 360/number_of_sides
    tim.color(random.choice(colors))
    draw_shape(angle, number_of_sides)

screen = Screen()
screen.exitonclick()



