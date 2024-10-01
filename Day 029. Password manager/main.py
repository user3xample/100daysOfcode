#! /usr/bin/env python3

#  THIS IS NOT SECURE DONT USE IN REAL LIFE
from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v','w','x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q',
              'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters =[choice(letters) for _ in range(randint(8, 10))]
    password_symbols =[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers =[choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entries.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) ==0 or len(password) ==0:
        messagebox.showifo(title="Oops", message="Please dont leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n\nEmail/Username:/"
                                                              f" {email}\nPassword: {password}\nWebsite: {website}/"
                                                              f" \n\nIs it ok to save?")

        if is_ok:  # If true do this, if not dont.
            with open("data.txt", "a") as data_file:  # This will open and close the file automaticly.
                data_file.write(f"{website} | {email} | {password}\n")
                website_entries.delete(0, END)
                password_entry.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="alogo.png")
canvas.create_image(100, 100, image=logo_img)  # x, y position so half of 200 height width. middle of logo.
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

#enteries
website_entries = Entry(width=55)
website_entries.grid(row=1, column=1, columnspan=2)
website_entries.focus()
email_entry =Entry(width=55)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "Users@email.com")
password_entry = Entry(width=36)
password_entry.grid(row=3, column=1)

#buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()