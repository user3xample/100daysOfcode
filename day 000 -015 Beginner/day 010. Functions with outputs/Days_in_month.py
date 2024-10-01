#! /usr/bin/env python3
# my version 19 lines
def days_in_month(year, month):
    if len(str(year)) < 3:
        return "error - our year is incorrect format. [xxxx]"
    if month < 1 or month > 12:
        return "error - our month is incorect [ 1 to 12]"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
                month_days[1] = 29
            else:
                leap_year = False
        else:
            leap_year = True
            month_days[1] = 29
    else:
        leap_year = False
    return month_days[month - 1]

##Anglea's############# 17 lines
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print("Leap year.")
#             else:
#                 print("Not leap year.")
#         else:
#             print("Leap year.")
#     else:
#         print("Not leap year.")

# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month - 1]




# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)