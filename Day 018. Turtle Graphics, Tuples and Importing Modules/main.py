#! /usr/bin/env python3

from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green")
def create_square():
    turns = 0

    for _ in range(4):  # Create square
        tim.forward(100)
        tim.right(90)
        turns += 1

def create_dash_line():
    rounds = 20

    for _ in range(rounds):
        tim.pendown()
        tim.forward(10)
        tim.penup()
        tim.forward(10)



# def set_mypen_color():  # While this works intherory not all colors are avaliable
#     r = random.randint(1, 255)
#     g = random.randint(1, 255)
#     b = random.randint(1, 255)
#     return tim.color(r, g, b)



def draw_shit():
    tim.pensize(15)

    colors4tim = ['red', 'blue', 'green', 'yellow', 'orange']
    direction = [0, 90, 180, 270]

    tim.setheading(random.choice(direction))
    tim.color(random.choice(colors4tim))
    tim.forward(100)






for n in range(0-100):
    draw_shit()



screen = Screen()
screen.exitonclick()