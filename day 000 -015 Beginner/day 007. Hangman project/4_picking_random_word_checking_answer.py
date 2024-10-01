#! /usr/bin/env python3
import random
# 1_picking_random_word_checking_answer.py
'''
  # todo1 - create a var called lives. set to 6.
  # todo2 - each guess thats not in the chosen word should reduce lives by one and stop and lose if you hit 0
  # todo3 - print each stage for each wrong answer.
'''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(" ---Welcome to hangman---\n")
lives = 6
word_list = ["aardvark", "baboon", "camel"]  # our word list
chosen_word = random.choice(word_list)  # Randomly chosen word
length_of_word = len(chosen_word)  # length of the chosen word
print(f"cheat: {chosen_word}")
display = []
end_of_game = False  # Flip flop switch to end the Game_0ne.


for char in chosen_word:  # we create our display of "_" for each char in the chosen word
    display += "_"

print((stages[lives]))
print(display)

while not end_of_game:
    guess = input("Please guess a letter: ").lower()  # Our users guess

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
        print(f"'{guess}' is not in the word")
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

print(" ---GAME OVER---")
