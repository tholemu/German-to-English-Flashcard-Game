from tkinter import *
import pandas
import json
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_json = {}

try:
    data = open("data/words_to_learn.json")
except FileNotFoundError:
    file = open("data/basic_words_in_german.json")
    words_json = json.load(file)
else:
    words_json = json.load(data)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_json)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(card_background, image="")
    flip_timer = window.after(5000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image="")


def is_known():
    words_json.remove(current_card)
    file_to_learn = open("data/words_to_learn.json", "w+")
    file_to_learn.write(json.dumps(words_json))
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(5000, func=flip_card)

canvas = Canvas(width=800, height=526)
# card_front_img = PhotoImage(file="images/card_front.png")
# card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image="")
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 264, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image="", highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# right_image = PhotoImage(file="images/right.png")
known_button = Button(image="", highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()