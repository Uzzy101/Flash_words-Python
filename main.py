from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

words_dict = {}
current_card = {}


try:
    lang_file = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_file = pandas.read_csv('data/french_words.csv')
    words_dict = original_file.to_dict(orient='records')
else:
    words_dict = lang_file.to_dict(orient='records')


def new_text_r():
    global current_card, flip_timer

    canvas_1.after_cancel(flip_timer)
    current_card = random.choice(words_dict)

    canvas_1.itemconfig(canvas_image, image=card_front)

    canvas_1.itemconfig(title_text, fill='black', text='French')
    canvas_1.itemconfig(word_text, fill='black', text=current_card['french'])

    # canvas_1.itemconfig(title_text, text='French')
    # canvas_1.itemconfig(word_text, text=current_card['french'])

    flip_timer = canvas_1.after(3000, func=check_back)


def new_text_w():
    global current_card
    words_dict.remove(current_card)
    data = pandas.DataFrame(words_dict)
    data.to_csv('data/words_to_learn.csv', index=False)
    new_text_r()


def check_back():
    global current_card
    canvas_1.itemconfig(canvas_image, image=card_back)

    canvas_1.itemconfig(title_text, fill='white', text='English')
    canvas_1.itemconfig(word_text, fill='white', text=current_card['english'])

    # canvas_1.itemconfig(title_text, text='English')
    # canvas_1.itemconfig(word_text, text=current_card['english'])


window = Tk()
window.title('Flash')
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

# Cards
canvas_1 = Canvas(width=800, height=600, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back = PhotoImage(file='images/card_back.png')
card_front = PhotoImage(file='images/card_front.png')
canvas_image = canvas_1.create_image(400, 300, image=card_front)
canvas_1.grid(row=1, column=2, columnspan=2)
title_text = canvas_1.create_text(400, 170, text='', fill='black', font=('Ariel', 40, 'italic'))
word_text = canvas_1.create_text(400, 280, text='', fill='black', font=('Ariel', 40, 'bold'))
flip_timer = canvas_1.after(5000, func=check_back)

# Wrong
canvas_2 = Canvas(width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR)
wrong = PhotoImage(file='images/wrong.png')
canvas_2.create_image(50, 50, image=wrong)
canvas_2.grid(row=3, column=2)
wrong_button = Button(window, image=wrong, border=0, command=new_text_r)
wrong_button.grid(row=3, column=2)

# Right
canvas_3 = Canvas(width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR)
right = PhotoImage(file='images/right.png')
canvas_3.create_image(50, 50, image=right)
canvas_3.grid(row=3, column=3)
right_button = Button(window, image=right, border=0, command=new_text_w)
right_button.grid(row=3, column=3)

new_text_r()

window.mainloop()
