#! /usr/bin/env python3

# tip_calc.py
#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

# Welcome
print ("Welcome to the tip calculator.")

bill = float(input("What was the total bill? £"))  #£150
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))  # 12
people = int(input("How many people to split the bill? "))  # 5

bill_with_a_tip = tip / 100 * bill + bill

total_bill = bill_with_a_tip / people
amount_to_pay = "{:.2f}".format(total_bill)  # This makes our amount to 2 places rather than £33.6

message = f"Each person should pay: £ {amount_to_pay}"
print(message)