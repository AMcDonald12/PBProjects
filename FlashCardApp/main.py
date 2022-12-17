from tkinter import *
from pandas import *
import random
BACKGROUND_COLOR = "#B1DDC6"

#--------------Load Words---------------#
try:
    word_csv=read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    word_csv=read_csv('data/spanish_words.csv')
finally:
    word_bank=word_csv.to_dict(orient='records')
    current_card = {}

#--------------Functions----------------#

def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_bank)
    canvas.itemconfig(card_color, image=card_front)
    canvas.itemconfig(card_title, text="Spanish", fill='black')
    canvas.itemconfig(card_word, text=current_card['Spanish'], fill='black')
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_color, image=card_back)
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')

def remove_card():
    word_bank.remove(current_card)
    data = DataFrame(word_bank)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_word()

#-------------- UI -------------#
#Initialize window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#Flash Card
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')

canvas = Canvas(height=526, width=800)
card_color = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="Title")
card_word = canvas.create_text(400, 263, font=("Ariel", 60, 'bold'), text="word")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness = 0)
canvas.pack()
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
wrong = PhotoImage(file='images/wrong.png')
right = PhotoImage(file='images/right.png')

wrong_button = Button(image=wrong, highlightthickness=0, command=next_word)
right_button = Button(image=right, highlightthickness=0, command=remove_card)

wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

next_word()

window.mainloop()