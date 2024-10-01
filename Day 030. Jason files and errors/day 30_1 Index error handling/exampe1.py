#! /usr/bin/env python3

fruits = ["apple", "Pear", "orange"]

#todo catch the exception and make sure the code can run

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print(f"Error: Make Pie Index Value '{index}' not found")
    else:
        print(fruit + " Pie")



make_pie(4)