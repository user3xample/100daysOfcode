#! /usr/bin/env python3

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()  # state is the first column in the file
guessed_states =[]


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} /50 states Correct", prompt="What's the name of another state?").title()
    print(answer_state) # for testing

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# If the answer_state is one of the states in all the states of the 50_states.csv
    # If they got it right:
        # Create a turtle to write the name of the state at the states x and y coor




screen.exitonclick()