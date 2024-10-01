#! /usr/bin/env python3

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split()}

print(result)
"""
{
    'What': 4,
    'is': 2,
    'the': 3,
    'Airspeed': 8,
    'Velocity': 8,
    'of': 2,
    'an': 2,
    'Unladen': 7,
    'Swallow?': 8
}
"""