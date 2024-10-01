#! /usr/bin/env python3
import turtle
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 60, "normal")
TOP_SCORE = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.top_score = TOP_SCORE
        self.color("yellow")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score +=1
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):

        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
        self.goto(0, -60)
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)
