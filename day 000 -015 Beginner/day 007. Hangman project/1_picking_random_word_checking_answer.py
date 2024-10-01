#! /usr/bin/env python3
import random
# 1_picking_random_word_checking_answer.py
'''
  # todo1 - randomly choose a word from the list and assign to var chosen_word. DONE
  # todo2 - ask the user to guess a letter and assign their answer to a var called guess. mk lower case Done
  # todo3 - check if the letter the user guessed is one of the letters in the chosen word.
'''
#print(" ---Welcome to hangman---\n")
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
length_of_word = len(chosen_word)
guess = input("Please guess a letter: ").lower()

for char in chosen_word:
    if char == guess:
        print(f"{guess}")
    else:
        print("-")







def test():
    print("\n ---Test ---")
    print(chosen_word)
    print(type(chosen_word))

test()

