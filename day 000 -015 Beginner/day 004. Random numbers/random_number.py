#! /usr/bin/env python3
import random


random_integer = random.randint(1, 10)
print("int: ",random_integer)

random_float = random.random()
print("flo: ",random_float)

random_float = random.random() * 5  # Produces a random 0- 4.99...
print("flo: ",random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")
