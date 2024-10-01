#! /usr/bin/env python3

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []
system_random = random.SystemRandom()

# choose letters
for opt1 in range(1, nr_letters +1, 1):
   choice = (system_random.randint(0,(len(letters)-1)))
   password += (letters[choice])

# Choose numbers
for opt2 in range(1, nr_numbers +1, 1):
   choice = (system_random.randint(0,(len(numbers)-1)))
   password += (numbers[choice])

#choose symbols
for opt3 in range(1, nr_symbols +1, 1):
   choice = (system_random.randint(0,(len(symbols)-1)))
   password += (symbols[choice])


output =""
random.shuffle(password)

for char in password:
    output += char

print(f"Your password is :\n {output}")
output = ""  # hopefully clearing the memory
password = ""
