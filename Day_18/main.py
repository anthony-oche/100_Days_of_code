from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ["lightslategray", "dimgray", "navy", "darkslategray", "seagreen", "darkolivegreen", "darkred"]

def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)

for shape_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_n)



























screen = Screen()
screen.exitonclick()