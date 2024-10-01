#! /usr/bin/env python3
import random
# 1_picking_random_word_checking_answer.py
'''
  # todo1 - create an empty list called display. "_" for each letter
  # todo2 - loop through each position display it if found
  # todo3 - print "display"
'''
print(" ---Welcome to hangman---\n")
word_list = ["aardvark", "baboon", "camel"]  # our word list
chosen_word = random.choice(word_list)  # Randomly chosen word
length_of_word = len(chosen_word)  # length of the chosen word
guess = input("Please guess a letter: ").lower()  # Our users guess
display = []


for char in chosen_word:  # we create our display of "_" for each char in the chosen word
    display += "_"

print(display)  # for test

index = 0  # my solution
for letter in chosen_word:
    if letter == guess:
        display[index] = letter
        index += 1
    else:
        index += 1

print(display)


# for position in range (length_of_word):  # Courses solution, probbably more efficient lol
#     letter = chosen_word [position]
#     if letter == guess:
#        display[position] = letter


def test():
    print("\n ---Test ---")
    print(display)
    print(chosen_word)
    print(type(chosen_word))

# test()

