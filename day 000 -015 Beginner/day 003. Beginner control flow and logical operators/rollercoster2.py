#! /usr/bin/env python3

print ("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:  # Greater than and equal
    # True
    print ("you can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are £5.")
        bill += 5
    elif age <= 18:
        print("Youth tickets are £7.")
        bill += 7
    elif age >= 45 and age <= 55:
        print("Lonely hearts club is free")
    elif age < 45:
        print("Adult tickets are £12.")
        bill += 12


    wants_photo = input(str("Do you want a photo taken? Y or N. ",))
    if wants_photo.upper() == "Y":  # force the input to uppercase
        print("That will be £3.")
        bill += 3


    print(f"Your final bill is £{bill}")
else:
    # False
    print("Sorry, you have to grow taller before you can ride.")
