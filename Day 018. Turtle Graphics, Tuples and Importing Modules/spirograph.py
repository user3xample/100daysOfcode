#! /usr/bin/env python3

import turtle as t
from turtle import Screen
import random

t.colormode(255)
tim = t.Turtle()
tim.speed(0)
tim.pensize(2)
size = 150  # size of circle
tilt = 60  # degrees


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r, g, b)
    return my_color


def draw_spiro(tilt):
    for _ in range(int(360 / tilt)):
        tim.color(random_color())
        tim.circle(size)
        tim.setheading(tim.heading() + tilt)


draw_spiro(tilt)
screen = Screen()
screen.exitonclick()
