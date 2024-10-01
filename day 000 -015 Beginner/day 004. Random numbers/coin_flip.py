#! /usr/bin/env python3

import random
heads = 0
tails = 0
rounds = 10_000_000

while rounds >= 1:
    flip = random.randint(0,1)
    if flip == 1:
        #print("Heads")
        heads += 1
        rounds -= 1
        
    else:
        #print("Tails")
        tails +=  1
        rounds -=  1


print(f"heads: {heads}\ntails: {tails} ")
print(heads + tails)