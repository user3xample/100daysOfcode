#! /usr/bin/env python3

# nesting.py

# nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a list in a Dictionary

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

["A", "B", ["C", "D"]] # List within a list.

# Nesting Dictionary in a Dictionary

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "France2": {"cities_visited":["Paris", "Lille", "Dijon"],"total_visits":12},  # god this is getting complexed real quick lol
    "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"],"total visits":5},
}

print (travel_log ["France2"])

# Nesting a dictionary inside a list
example = [{
    "Key":["List"],
    "key2":{dict},
},
{
     "Key": "Value",
    "key2": "value",
}
]

print( example [0])

# Nesting Dictionary in a list # Good idea to seperate them out to make easier to read.
travel_log2 = [
    {
        "country":"France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country":"Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total visits": 5
    },
]