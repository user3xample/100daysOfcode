#! /usr/bin/env python3
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# bmi = 40  # used for testing
bmi = round(weight / height ** 2)

# Under 18.5 they are underweight
if bmi <= 18.5:
    message = "are underweight."

# Over 18.5 but below 25 they have a normal weight
elif bmi <= 25:
    message = "have a normal weight."

# Over 25 but below 30 they are slightly overweight
elif bmi <= 30:
    message = "are slightly overweight."

# Over 30 but below 35 they are obese
elif bmi <= 35:
    message = "are obese."

# Above 35 they are clinically obese.
else:
    message = "are clinically obese."

print(f"Your BMI is {bmi}, you {message}")