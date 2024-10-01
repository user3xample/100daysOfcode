#! /usr/bin/env python3
# https://www.w3schools.com/colors/colors_rgb.asp  useful

import colorgram
from turtle import Screen
import turtle as t
import random
"""
Create your very own damian hurst Dots painting  This one evolves over time as the dots once
populated will keep chainging colour
"""

t.colormode(255)
tim = t.Turtle()
tim.speed(0)
active = True
#
# number_of_colors = 50
# image_location = "image.jpg"
# paint_pot = []
#
# colors_in_image= colorgram.extract(image_location, number_of_colors)  # will only pull the max in image.
# for color in colors_in_image:
#      r = color.rgb.r
#      g = color.rgb.g
#      b = color.rgb.b
#      new_color = (r, g, b)
#      paint_pot.append(new_color)
# print(paint_pot)
# print(f"\nUnique Colours added to paint pot:  {len(paint_pot)}")
# # This section isnt used all the time and can be commented off to help with speed.
# # I have also removed the first 4 colours in our paint pot as they were white.

paint_pot = [
    (196, 159, 118), (150, 87, 46),(48, 106, 144),
    (133, 167, 186), (189, 143, 159), (144, 68, 91), (13, 27, 58), (185, 154, 29), (56, 25, 13), (134, 178, 165),
    (63, 19, 34), (51, 123, 98), (218, 203, 133), (130, 29, 53), (188, 89, 115), (149, 28, 15), (15, 48, 35),
    (12, 98, 61), (222, 173, 185), (57, 164, 144), (199, 94, 76), (23, 54, 124), (51, 158, 176), (88, 87, 13),
    (163, 207, 197), (227, 174, 166), (10, 88, 103), (106, 120, 163), (160, 205, 212), (179, 187, 213), (242, 201, 6),
     ]

tim.penup()
tim.hideturtle()
# tim.setheading(225)
# tim.forward(900)  # diagonal
# tim.setheading(180)  # face left
# tim.forward(550) # travel left botom row
# tim.setheading(0)
# start_point = tim.position()
# print(start_point)

def paint_me():
    number_of_dots = 1296
    tim.goto(-1186.40,-636.40)  # Our start point of the page bottom left.
    #print(tim.position())
    for dot_count in range(1, number_of_dots + 1):
        #print(tim.position())
        tim.dot(20, random.choice(paint_pot))
        tim.forward(50)
        if dot_count >= number_of_dots:
            tim.speed(1)
            #print("lowered speed, now looping")
            paint_me()

        elif dot_count % 48 == 0:  # 48 dots , used to go up a line and start again
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(2400)
            tim.setheading(0)


paint_me()


screen = Screen()
screen.exitonclick()






