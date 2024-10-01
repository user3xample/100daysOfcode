#! /usr/bin/env python3

from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Create a random red apple"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
