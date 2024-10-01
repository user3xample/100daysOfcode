#! /usr/bin/env python3
import random
# 1_picking_random_word_checking_answer.py
'''
  # todo1 - use a while loop to let the user guess again. the loop should only stop
 once all the letters in the chosen word and display has no more blanks then tell the user they  won
'''
print(" ---Welcome to hangman---\n")
word_list = ["aardvark", "baboon", "camel"]  # our word list
chosen_word = random.choice(word_list)  # Randomly chosen word
length_of_word = len(chosen_word)  # length of the chosen word
print(f"cheat: {chosen_word}")
display = []
end_of_game = False  # Flip flop switch to end the Game_0ne.

for char in chosen_word:  # we create our display of "_" for each char in the chosen word
    display += "_"

print(display)  # for test
while not end_of_game:
    guess = input("Please guess a letter: ").lower()  # Our users guess

    index = 0  # my solution
    for letter in chosen_word:
        if letter == guess:
            display[index] = letter
            index += 1
        else:
            index += 1

    print(display)

    if "_" not in display:  # Our flip flop switch to end the Game_0ne
        end_of_game = True
    print(" ---YOU WIN---")
print(" ---GAME OVER---")
