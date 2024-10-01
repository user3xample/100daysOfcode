#! /usr/bin/env python3
# Uses turtle https://docs.python.org/3.3/library/turtle.html

from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)  # pixel x pixel
screen.bgcolor("black")
screen.title("White lines Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.105)

    snake.move()

screen.exitonclick()
