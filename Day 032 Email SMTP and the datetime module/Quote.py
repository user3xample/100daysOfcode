#! /usr/bin/env python3

import smtplib
import datetime as dt
import random

my_email = "user3xample.projects@gmail.com"
password = "dhnfybugwdtizmrj"
email_list = ["paul.abel@gmx.com", "lauren.merron@hotmail.com"]
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open ("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    for mailto in email_list:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Very important, make secure always.
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=f"{mailto}",
                msg=f"Subject:Monday Motivational Quote\n\nHello there,\n\nHere is your"
                    f" motivational quote for a Monday.\n\n{quote}\n\nWishing you a Great Day."
                    f"\n\n\nKind Regards\n\nUser3xample\n\n\n"
                    f"(reply back STOP to stop the quotes this can take 24hrs+ to do.)"
            )
            connection.close()
