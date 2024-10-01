#! /usr/bin/env python3

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enimies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")