#! /usr/bin/env python3
import os
from art import logo
def clear_screen():
    os.system('cls||clear')

# caesar_cipher_encryption.py
print(f"{logo}")  # from our art.py file
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
alphabet += alphabet  # so we can shift of 26 if needed.
repeat = True


def caesar(direction, text, shift):
    output = ""
    if direction == "decode":
        shift *= -1  # This reverses our shift.
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            output += alphabet[position + shift]  # Now we add to our output
        else:
            output += char  # If not in our alphabet then we add it as plain text.
    print(f"Here's the {direction}d result:\n{output}\n")

while repeat :

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26  # This stops stupid sized shift numbers we just rotate around the 26 letters.

    caesar(direction, text, shift)
    choice = input("Would you like to use again? 'y' or 'n' :\n")
    if choice == "n":
        repeat = False
    clear_screen()

clear_screen()
print(f"{logo}")
print(" ---Bye---")