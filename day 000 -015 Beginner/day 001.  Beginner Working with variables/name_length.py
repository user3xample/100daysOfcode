#! /usr/bin/env Python3
# Code snipit to work out the length of a string that is provided by a user input.

s= input ("What is your name? ")
print(len(s))  # To get the length of the string that was provided
#or
print(len(input("What is your name? ")))

# bonus stuff i found

import sys
a = sys.getsizeof(s)
print(f"The size in bytes is: {a}")

