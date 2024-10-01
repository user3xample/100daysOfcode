#! /usr/bin/env python3
import os
os.system('cls||clear')
# caesar_cipher_encryption.py

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
alphabet += alphabet  # so we can shift of 26 if needed.
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        cipher_text += alphabet[position + shift]
    print(f"The encoded text is:\n{cipher_text}")

def decrypt(text, shift):
    plain_text = ""
    for letter in text:
        position = alphabet.index(letter)
        plain_text += alphabet[position - shift]
    print(f"The decoded text is:\n{plain_text}")


if direction == "encode":
    encrypt(text, shift)

elif direction == "decode":
    decrypt(text, shift)
else:
    print(f"error - {direction} is not a valid option.")
