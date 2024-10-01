#! /usr/bin/env python3
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

list_length = (len(names))  # Work out the list length
random_integer = random.randint(0,list_length -1)  # choose a random number between 0 and the length of list
bill_payer = (names [random_integer])  # pick the name that is the random number
print(f"{bill_payer} is going to buy the meal today!")  # print our output.