#! /usr/bin/env python3


from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

#  We look for our saved file of personal words if not found we use the original to start off.
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # cancels the timer so we can start again.
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    # index set to False, so we don't save the index numbers
    next_card()


# def rules():
#     messagebox.showinfo(title="How to Use", message="How to use:",)# font=("Ariel", 12, "bold"))


window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # pulling our colour down.
flip_timer = window.after(3000, func=flip_card)

# canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="<placeholder_Title>", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263, text="<placeholder_word>", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# buttons
    # right
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button (image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=1)
    # left
check_image = PhotoImage(file="images/right.png")
known_button = Button (image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=0)


next_card()  # To show the first card as we load.






#rules()
window.mainloop()