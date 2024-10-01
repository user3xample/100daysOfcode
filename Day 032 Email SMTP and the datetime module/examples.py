#! /usr/bin/env python3

import smtplib

my_email = "emailaddress"
password = "password"
#  dont ever do this its bad practice never hard code creds
mailto = input("What is the email address to receive the message: ")
subject = input(str("Whats the subject line: "))
message = input(str("What is our message: "))

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # make secure
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=f"{mailto}",
        msg=f"Subject:{subject}\n\n{message}"
    )
    connection.close()
print("[*] Message sent")
print(f"[*] mailto: {mailto}\nSubject: {subject}\n\n'{message}'")



