#! /usr/bin/env python3

# https://docs.python.org/3/library/tkinter.html#the-packer
#import tkinter
from tkinter import *  # Can also do like this then drop the tkinter at the start.

#window = tkinter.Tk()
window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

# Label

#my_label = tkinter.Label(text="I'm a Label", font=("Arial", 24, "bold"))
my_label = Label(text="I'm a Label", font=("Arial", 24, "bold"))
my_label.pack()  # expand=True, side="top"
my_label.config(padx=50, pady=50)

my_label["text"] = "new text"  # can set like this
my_label.config(text="New Text")  # or like this.
my_label.grid(column=0, row=0)
# Button
def button_clicked():
    print("i was clicked")
    my_label.config(text = input.get())  # remember we could have used the other way too.

# button 1
button1 = Button(text="buton1", command=button_clicked)
button1.grid(column=1, row=1)
# button 2
button2 = Button(text="button2", command=button_clicked)
button2.grid(column=2, row=0)

# Entry

input = Entry(width= 20)
input.grid(column=3, row=2)







window.mainloop()  # always has to be at the bottom