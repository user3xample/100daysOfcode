#! /usr/bin/env python3
# fiz_buzz.py

for number in range (1, 101, 1):
    if (number %5 == 0) and (number % 3== 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

