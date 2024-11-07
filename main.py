from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
try:
    dataframe = pandas.read_csv("data/words_to_learn.csv")
except:
    dataframe = pandas.read_csv("data/french_words.csv")

words_to_learn = dataframe.to_dict(orient="records")          # with this orientation to_learn is a list of dictionary containing key and values

def next_card():
    global flip_timer,current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)  #here current_card is a dictionary which has two keys French and English and their corresponding values
    canvas.itemconfig(card_image, image= card_front)
    canvas.itemconfig(title_text, text = "French", fill = "black")
    canvas.itemconfig(word_text, text= current_card["French"], fill ="black")


    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title_text, text = "English", fill= "white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image= card_back)

def remove_known_card():
    words_to_learn.remove(current_card)
    # change list of dictionary to dataframe i.e using pandas to create dataframe
    df = pandas.DataFrame(words_to_learn)
    # save dataframe as csv
    with open("data/words_to_learn.csv", mode= "w") as file:
        pass
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()










window = Tk()
flip_timer = window.after(3000, flip_card)

#.............UI SETUP.........................#
window.title("FlashCARD")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)

canvas = Canvas(width= 800, height= 526, bg= BACKGROUND_COLOR, highlightthickness= 0)
card_back = PhotoImage(file= "images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400, 263, image= card_front)
title_text = canvas.create_text(400, 100, text= "", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 270, text= "", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan =2)

rightmark = PhotoImage(file="images/right.png")
wrongmark = PhotoImage(file="images/wrong.png")

unknown_button = Button(image=wrongmark, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=rightmark, highlightthickness=0, command=remove_known_card)
known_button.grid(row=1, column=1)

next_card()


window.mainloop()


