#! /usr/bin/env python3
# import another_module
# print(another_module.another_variable)  # returns 12


#import turtle
# #timmy = turtle.Turtle()
#
# # or we could just do:
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("Darkgreen")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["pikachu", "something", "something else"])
table.add_column("Type", ["Electric", "fire", "water"])
table.align = "l"
print(table.align)

print(table)

x = PrettyTable()
x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])
#or
# x.add_rows(
#     [
#         ["Adelaide", 1295, 1158259, 600.5],
#         ["Brisbane", 5905, 1857594, 1146.4],
#         ["Darwin", 112, 120900, 1714.7],
#         ["Hobart", 1357, 205556, 619.5],
#         ["Sydney", 2058, 4336374, 1214.8],
#         ["Melbourne", 1566, 3806092, 646.9],
#         ["Perth", 5386, 1554769, 869.4],
#     ]
# )
print(x)
print(x.get_string(fields=["City name", "Population"]))