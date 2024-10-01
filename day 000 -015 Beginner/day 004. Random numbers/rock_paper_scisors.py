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



my_choice = input(" input 1 for rock, 2 for paper or 3 for scissors.  Your choice is : ")
my_choice = int(my_choice)
if my_choice == 1:
    print("You choose Rock")
    print(rock)
elif my_choice == 2:
    print("You choose Paper")
    print(paper)
elif my_choice == 3:
    print("You choose Scissors")
    print(scissors)
else:
    print("error - you tried to cheat.  Game_0ne over")
    exit(0)

cpu_choice = random.randint(1,3)

if cpu_choice == 1:
    print("Computer chooses Rock")
    print(rock)
elif cpu_choice == 2:
    print("computer chooses Paper")
    print(paper)
elif cpu_choice == 3:
    print("computer chooses Scissors")
    print(scissors)

lose = "You lose"
win = "You win"
draw = "Its a Draw"

if cpu_choice==1:  # rock
    if cpu_choice ==1 and my_choice==1:  # rock vs rock
        print (draw)
    elif cpu_choice ==1 and my_choice==2:  # rock vs paper
        print (lose)
    elif cpu_choice ==1 and my_choice==3:  # rock vs scisors
        print(win)
elif cpu_choice==2:  # paper
    if cpu_choice ==2 and my_choice==1:  # rock vs paper
        print (lose)
    elif cpu_choice ==2 and my_choice == 2:  # paper vs paper
        print (draw)
    elif cpu_choice ==2 and my_choice == 3:  # rock vs scisors
        print(win)
elif cpu_choice==3:  # scisors
    if cpu_choice ==3 and my_choice==1:  # rock vs scisios
        print (win)
    elif cpu_choice ==3 and my_choice == 2:  # paper vs scisors
        print (lose)
    elif cpu_choice ==3 and my_choice == 3:  # scisiors vs scisors
        print(draw)