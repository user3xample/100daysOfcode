#! /usr/bin/env python3

with open("my_file.txt") as file:
    content = file.read()
    print(content)

# r = read, w = write a= append
with open("new_file.txt", mode="w") as file:
    file.write("New text")


