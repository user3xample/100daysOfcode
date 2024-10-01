#! /usr/bin/env python3

# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return  f"{formatted_f_name} {formatted_l_name}"
#
# # we could do this
# print(format_name("paul", "abel"))
#
# # We can also do this
# print(format_name(input("What is your first name? "),input("What is your last name? ")))

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":  # by adding this we return early if blank's are inputted.
        return "error - you didnt provide valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return  f"{formatted_f_name} {formatted_l_name}"

# we could do this
print(format_name("paul", "abel"))

# We can also do this
print(format_name(input("What is your first name? "),input("What is your last name? ")))