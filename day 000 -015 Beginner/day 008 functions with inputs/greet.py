#! /usr/bin/env python3
# greet.py

# Review:
# create a function called greet().
# Write 3 print statements inside the function.
# call the greet() function and run your code.

# Simple
# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")
#
# greet()

# function that allows for inputs

def greet_with_name(name):

    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("michelle")
# name is the parameter
# michelle is the argument

# More than one parameter
def greet_with(name, location):
    print(f"Hello {name} how is the weather in {location} today?")

greet_with("michelle", "london")  # This is positional argument
greet_with(location = "usa", name = "paul")  # we can use this too in any order. Keyword argument