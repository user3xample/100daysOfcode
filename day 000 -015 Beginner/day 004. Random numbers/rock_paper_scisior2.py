#! /usr/bin/env python3
import random

# rock paper scissors with if statements

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("---RPS champion---\n")

my_choice = int(input(" input 0 for rock, 1 for paper or 2 for scissors.  Your choice is : "))
cpu_choice = random.randint(0,2)

if my_choice < 0 or my_choice >2 :
    print ("invalid choice You loose")
    exit(0)
elif my_choice == 0:
    print("your choice 'Rock'")
    print(rock)
elif my_choice == 1:
    print("your choice 'Paper'")
    print(paper)
elif my_choice == 2:
    print("your choice 'Scissors'")
    print(scissors)



if cpu_choice == 0:
    print("Computer choice 'Rock'")
    print(rock)
elif cpu_choice == 1:
    print("Computer choice 'Paper'")
    print(paper)
elif cpu_choice == 2:
    print("Computer choice 'Scissors'")
    print(scissors)

# user->  0   1     2
com_0 = ["Draw","️You Win","️You Lose"]
com_1 = ["You Lose","Draw","️You Win"]
com_2 = ["You Win","️You Lose","Draw"]
map = [com_0, com_1, com_2]

horizontal = my_choice  # get our first position ->
vertical = cpu_choice  # get our second |

print(map[vertical][horizontal])