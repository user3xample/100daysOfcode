#! /usr/bin/env python3
# Uses turtle https://docs.python.org/3.3/library/turtle.html

from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)  # pixel x pixel
screen.bgcolor("black")
screen.title("Apple Munching Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #  Detect collision with food.
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #  Detect collision with wall.
    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    #  Detect collision with the body / tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
