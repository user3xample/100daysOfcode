#! /usr/bin/env python3

print ("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height >= 120:  # Greater than and equal
    # True
    print ("you can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay £5.")
    elif age <= 18:
        print("Please pay £7.")
    else:
        print("Please pay £12.")
else:
    # False
    print("Sorry, you have to grow taller before you can ride.")

