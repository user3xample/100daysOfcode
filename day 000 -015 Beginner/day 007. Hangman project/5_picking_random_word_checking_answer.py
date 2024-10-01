#! /usr/bin/env python3
import random
import hangman_words
from hangman_art import logo, stages  # Import the ascii art banner, Import the hangman stages
from os import system, name  # Used for our clear function
# 1_picking_random_word_checking_answer.py
'''
  # todo1 - update the wordlist from hangman_words.py
  # todo2 - remove the previous words
  # todo3 - use the logo at the start.
'''
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')



banner = logo
print(f"{banner}")

chosen_word = random.choice(hangman_words.word_list)  # Randomly chosen word from our wordlist file
length_of_word = len(chosen_word)  # length of the chosen word
end_of_game = False  # Flip flop switch to end the Game_0ne.
display = []
lives = 6  # Set the amount of lives we have

print(f"cheat: {chosen_word}")  # For testing remove

for char in chosen_word:  # we create our display of "_" for each char in the chosen word
    display += "_"

print((stages[lives]))
print(display)

while not end_of_game:

    guess = input("Please guess a letter: ").lower()  # Our users guess
    clear()
    if guess in display:
        print(f"You've already guessed '{guess}'")

    index = 0  # my solution
    for letter in chosen_word:
        if letter == guess:
            display[index] = letter
            index += 1

        else:
            index += 1

    if guess not in chosen_word:  # Adjust our display and lives counter
        lives -= 1
        print(stages[lives])
        print(f"'{guess}' is not in the word, life lost.")
    elif guess in chosen_word:
        print(stages[lives])
        print(f"'{guess}' is in the word!")

    if lives == 0:
        print("You are out of lives!!\n ---YOU LOSE---\n")
        end_of_game = True

    if "_" not in display:  # Our flip flop switch to end the Game_0ne
        end_of_game = True
        print(f"Correct the chosen word was {chosen_word}\n ---YOU WIN---\n")

    print(display)  #Show our display and what guesses we got left
    print("-" *50)

print(" ---GAME OVER---")

# end
