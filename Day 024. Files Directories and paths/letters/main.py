#! /usr/bin/env python3

PLACEHOLDER = "[name]"

with open("./input/Names/invited_names.txt","r") as names_file:
    names = names_file.readlines()


with open("./input/letters/starting_letter.txt","r") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(f"./output/readyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)