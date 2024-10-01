#! /usr/bin/env python3

# https://docs.python.org/3/library/tkinter.html#the-packer
#import tkinter
from tkinter import *  # Can also do like this then drop the tkinter at the start.

window = Tk()
window.title("Miles to KM converter")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)

# Label

miles_label = Label(text="Miles", font=("Arial", 20))
miles_label.grid(row=0, column=2)
miles_label.config(padx=5, pady=5)

km_label = Label(text="KM", font=("Arial", 20))
km_label.grid(row=1, column=2)
km_label.config(padx=5, pady=5)

result_label = Label(text="0", font=("Arial", 40))
result_label.grid(row=1, column=1)
result_label.config(padx=5, pady=5)

is_equal_label = Label(text="Is Equal too:", font=("Arial", 20))
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=5, pady=5)

# Button
def button_clicked():
    miles = miles_input.get()
    km_result = float(miles) * 1.609
    result_label.config(text=f"{km_result}")

# button 1
calculate = Button(text="Calculate", command=button_clicked, font=("Arial", 15))
calculate.grid(row=2, column=1)

# Entry
miles_input = Entry(width= 10, font=("Arial", 20) )
miles_input.grid(row=0, column=1)

window.mainloop()  # always has to be at the bottom