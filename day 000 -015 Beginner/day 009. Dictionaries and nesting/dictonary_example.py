#! /usr/bin/env python3

thisdict =	{
    "Key": "Value",     # we can use str : str
    1: 123,             # int:int
    "year": 1964,       # str: int anything really
}
# Retrieving items from dictionary.
print(thisdict["year"])

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

# Retrieving items from dictionary.
print(programming_dictionary["Function"])

# Retrive all items
print(programming_dictionary)

# Adding new items to dictionary.
programming_dictionary ["new"] = "our new dictionary item is added like this"

print(programming_dictionary["new"])

# create an empty dictionary
empty_dictionary = {}

# Edit an item
programming_dictionary["Bug"] = "Changed"

print(programming_dictionary["Bug"])

# looping through a dictionary
for thing in programming_dictionary:
    print(thing)  # This will only print out the Key (first word)
    print(programming_dictionary["Bug"])  # This will give us the text (value)