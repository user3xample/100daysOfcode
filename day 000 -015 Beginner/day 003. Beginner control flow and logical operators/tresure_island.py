#! /usr/bin/env python3

chest = ('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")
line = ("-" *50)

print(line)
print("rules:\nEvery time you see a word as part of a question in 'quotes' its your word to use for your choice.")
print("Secondly no cheating stick to the choice words.\n")
print(line)
print("Lets start---\n")
print("Enter stage right our Hero, our Adventurer! in your bright shinny suit of armour. ta dahhhh!!")

name = input("Wait, wait, WAIT... I nearly forgot first every adventurer needs a name, whats yours my friend? : ").lower()


cheat =(f"""\nSadly you tried to cheat the story didn't you {name} and died.  
Yes died, loser!\n I guess I can be off now and just in time for tea.\n  ---GAME OVER---""")

if name == "jack":
    print(line)
    print("""
    \nJack you say!\nAll the fine names in the world for a hero... and you choose Jack?!!!
    I can see you not done this adventuring thing much have you 'Jack' ha ha  strange name for a
    strange child but funny that you say your name is Jack,  I know another story about a giant and
    a beanstalk that involved a Jack.  It didn't end well for the poor old giant
    But that's another story and will need to be told another day...
    """)
    # not called jack
elif name != "jack":
    print (f"   \n{name} you say! That is a mighty fine name is {name} a good choice for an adventurer.")
    print(" I remember there was this story about...\n")

# Preamble
print(f"""\nYes, yes, ok hold your horses I'll get on with our 'Treasure island' story. Jeeze patience of some people.
Now where was I ?...\n
Ah yes, you are walking down a road it's just outside a little village not too far from here {name}.
The road is a bit twisty and narrow with lots of trees either side and you cant see much through the brush
You know the type of fairytale roads dont ya {name} come on get your head in the game my dear adventurer.
It seems to go on for ages but...\n""")

    # first choice:
print(f"""Then You come to a junction do you turn 'left' or 'right'?\nQuick, quick, I cant be waiting all day I got a hot date with a succubus at midday,
oh the things she can do I tell you {name} they would make your eyes pop out !!""")

direction = input(str("Well whats it to be then? 'left' or 'right' ? : ")).lower()



    # right: first choice
if direction == "right":
    print(f"""\nSadly {name} {direction} was the wrong direction and you loose your footing sliding down a ravin.\n{name}... Someone shouts out 
    {name}!!...\nYou cant see who it is calling your name while falling...\nThere is a thud...\nthe world around you starts to go dark.
    You are no more you quickly die {name}\n!!!GAME OVER!!!""")
    # left: first choice
elif direction == "left":
    print(f"\nYou decide to go {direction} and this proves to be the correct way {name}.")
    # Second choice
    print(f"""You gradually head down the hill you are on, towards a big lake,You can see a castle
    on an island in the middle of the lake.  Its not that far a couple hundreed meters.
    You could easily swim across or walk round the lake to see if there is a bridge I guess but how longs that going to take?.""")

    walk_or_swim=input(str(f"What do you think you should do?  should you 'swim' or 'walk' {name}? : "))
    walk_or_swim = walk_or_swim.lower()
    # Swim: second choice
    if walk_or_swim == "swim":
        print(f"""\nOh dear, dear, me its like I have been talking to myself and I had such high hopes for you {name}.
        you clearly forgot I told you at the start you're wearing a suit of armour!\n
        ...You dont get far from the shore before the weight of the armour starts to drag you down.
        You reach round {name} desperately trying to get the buckles to undo as your lungs start to fill with water
        Its clearly too heavy and starts to drag you down into the murky depths of the lake never to be seen again...\n
          ---GAME OVER---
        \nRight well im off to the pub to go see Gracie the succubus.
        I Guess you could say 'She goes down nearly as quick as {name} in a suit of armor trying to swim',
        and the only one coming back up for air and it isn't you {name} ha ha.""")
    # walk: second choice
    elif walk_or_swim =="walk":
        print(f"""
        \nYou dont fancy your chances of swimming so you decide to walk
        it was probably the right idea after all {name} your wearing a suit of armour dont forget,
        that wouldn't have been a fine moment.  Its a lovely day and the sun is breaking out all over the place.\n
        Its not long till you get to the front of the island and castle.  Im guessing this as it has two huge towers 
        bearing down and a draw bridge that's luckily down. Red banners drapped either side.  Oh its a sight to see.\n
        What?!\n 
        You thought you was getting a nice castle image here didn't you {name}?\n
        Use your imagination, Im a ledgendry story teller not a f##cking ascii artist!\n
        And have you seen the budget for this {name}?!
        I mean not a pot to p....\n\n
        Yes, yes, back to the story...\n""")
        # choice 3
        print(f"""
        You walk into the castle admiring the decorations and the grandeur of it all. But its eerily quite I mean too
        quite and i dont see no treasure laying around.  They must have it all stashed away hidden.
        As you move further into the castle you head down into the lower levels you get to a room that has 3 doorways
        leading off of it.  There is something carved into the floor you read it out\n
        'Behind these 3 doors lie pleasure and pain,
        1 lies with treasures you will like.
        behind the other 2 lies a fright.'\n
        """)
        print(f"""{name} stands there wondering what all this could mean...\n
        ...I'm not sure why because it obvious to a seasoned adventure like myself there is 3 doors 1 has treasure,
        the other 2 yad yad yad.\n Right get on with it {name} I got a damsel in distress story coming up
        and i still havnt found a unicorn for it.  I haven't got all day to sit here telling a story.\n""")
        doors = input(str(f"What doors it to be {name} 'red', 'yellow' or 'blue' ? : "))
        doors = doors.lower()
        # choice 3 : red
        if doors == "red":
            print(f"""\nYou thought about it and decided to go through the {doors} door.
            The universal colour for stop, danger, so it was no f##king surprise it was the wrong door.
            You find yourself falling forwards into a pit full of red snakes.  Do ask me what ones they are
            i'm more worried how your getting out of here.
            ...Sadly {name} was never seen again but rumor has it there is one big fat snake in the castle.\n
              ---GAME OVER---
            """)
        # choice 3 : yellow
        elif doors == "yellow":
            print(f"""  \nYou thought about it and decided to go through the {doors} door.
            The universal color for yep you guessed it gold.  And lots of it in a big chest in the middle of the
            room.  Rumor has it {name} has a new castle of their own, and a dragon.  Everyone wants a dragon.\n
              ---WINNER---""")
            print(chest)
        # choice 3 : blue
        elif doors == "blue":
            print(f"""You thought about it and decided to go through the {doors} door.
            The universal color for water.  You find yourself falling forwards into a big dark well
            with water at the bottom and unfortunately you have no way of getting out.  But i wouldnt
            worry about that right now {name}, i would worry more about the thing that moved in the
            water next to you.  Slowly you find you are being dragged down into the murky water in the well
            never to be seen again.\n
              ---GAME OVER
            """)
        else:
            print(line)
            print("\n", cheat)
            print(line)
    else:
        print(line)
        print("\n", cheat)
        print(line)
else:
    print(line)
    print("\n", cheat)
    print(line)

# End ...Or is it.
