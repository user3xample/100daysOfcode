#! /usr/bin/env python3
total =0
for number in range (2, 101, 2):  # start, end, step
    total += number
  # we will add all numbers from 2 to 100 together to get the total if they are even.
print (total)

#  method 2
total_A =0
for number in range (1, 101, 1):  # start, end, step
    if number % 2 ==0:
        total_A += number
  # we will add all numbers from 2 to 100 together to get the total if they are even.
print (total_A)