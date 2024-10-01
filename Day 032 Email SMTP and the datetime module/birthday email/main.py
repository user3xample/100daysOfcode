#! /usr/bin/env python3

from datetime import datetime
import pandas
import random
import smtplib

# date and time
dt = datetime
today = dt.now()
today_tuple = (today.month, today.day)
# mail
my_email = "Email address goes here"
password = "gjfjhgfj£hgl"  # fake
#  in real life this is bad practice putting it hard coded. dont ever do this.
mailserver = "smtp.gmail.com"
# "smtp.gmail.com", "smtp.live.com" hotmail, "smtp.mail.yahoo.com", Outlook(smtp-mail.outlook.com)



data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]  # Check if the date is todays
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open (file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP(mailserver) as connection:
        connection.starttls()  # Very important, make secure always.
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )







