#! /usr/bin/env python3
import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

bet_locked_in = False
while not bet_locked_in:
    user_bet = screen.textinput(title="make your bet",
                                prompt=f"{colors}\nWhich turtle will win the race? Enter a colour: ").lower()
    if user_bet in colors:
        bet_locked_in = True


y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles=[]

for turtle_index in range (0, len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    new_turtle.width(5)
    new_turtle.pendown()
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 225:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win, {winning_color} was the winner!" )
                exit(0)
            else:
                print(f"You have lost {winning_color} was the winner!")
                exit(0)

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()