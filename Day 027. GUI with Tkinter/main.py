#! /usr/bin/env python3

# https://docs.python.org/3/library/tkinter.html#the-packer
#import tkinter
from tkinter import *  # Can also do like this then drop the tkinter at the start.

#window = tkinter.Tk()
window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=500)

# Label

#my_label = tkinter.Label(text="I'm a Label", font=("Arial", 24, "bold"))
my_label = Label(text="I'm a Label", font=("Arial", 24, "bold"))
my_label.pack()  # expand=True, side="top"

my_label["text"] = "new text"  # can set like this
my_label.config(text="New Text")  # or like this.

# Button


def button_clicked():
    print("i was clicked")
    my_label.config(text = input.get())  # remember we could have used the other way too.


button = Button(text="click Me", command=button_clicked)
button.pack()  # always need to pack things up with tkinter

# Entry

input = Entry(width= 50)
input.pack()






window.mainloop()  # always has to be at the bottom