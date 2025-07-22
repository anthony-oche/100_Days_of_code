import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet.", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "purple", "yellow", "orange"]
y_direction = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_direction[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner.")
            else:
                print(f"You've lost! The {winning_color} is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)























# def forward():
#     tim.forward(10)
# def backward():
#     tim.backward(10)
# def clockwise():
#     tim.setheading(tim.heading() + 10)
# def counter_clockwise():
#     tim.setheading(tim.heading() - 10)
# def clear_screen():
#     tim.reset()







# screen.listen()
# screen.onkey(fun=forward, key="w")
# screen.onkey(fun=backward, key="s")
# screen.onkey(fun=clockwise, key="d")
# screen.onkey(fun=counter_clockwise, key="a")
# screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()