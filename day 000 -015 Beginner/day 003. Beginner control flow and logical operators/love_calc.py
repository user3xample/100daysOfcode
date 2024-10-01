#! /usr/bin/env python3
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
#name1 = input("What is your name? \n")
#name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = str("Catherine Zeta Jones")
name2 = str("Michael Douglas")

combined_name = name1.lower() + name2.lower()

letter_t = int(combined_name.count("t"))
letter_r = int(combined_name.count("r"))
letter_u = int(combined_name.count("u"))
letter_e = int(combined_name.count("e"))
score_A = letter_t + letter_r + letter_u + letter_e
score_A = str(score_A)

letter_l = int(combined_name.count("l"))
letter_o = int(combined_name.count("o"))
letter_v = int(combined_name.count("v"))
letter_e = int(combined_name.count("e"))
score_B = letter_l + letter_o + letter_v + letter_e
score_B = str(score_B)

score = score_A+score_B
score = int(score)

if (score >= 40) and (score <= 50):
    message = ", you are alright together."
elif (score < 10) or (score > 90):
    message = ", you go together like coke and mentos."
else:
    message = ""

print(f"Your score is {score}{message}")