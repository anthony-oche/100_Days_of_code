import turtle
from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()

FONT = 'monaco', 8, "bold"


guessed_states = []


while len(guessed_states) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        # states you have to learn
        # for state in state_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        new_file = pandas.DataFrame(missing_states)
        new_file.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data["state"] == answer_state]
        # x_position = int(data[data.state == answer_state].x)
        # y_position = int(data[data.state == answer_state].y)
        x_position = data[data.state == answer_state]
        y_position = data[data.state == answer_state]
        t.goto(x_position.x.item(), y_position.y.item())
        t.write(answer_state, font=FONT)










