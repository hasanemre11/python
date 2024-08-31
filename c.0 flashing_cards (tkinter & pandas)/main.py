from tkinter import *
import pandas
import random

data = (pandas.read_csv(open(r"C:\Users\hasan\Desktop\python\yeni\20) flashing_cards\data\french_words.csv"))
        .values.tolist())
duo = random.choice(data)
f_word = duo[0]
e_word = duo[1]
print(f_word)

is_front = True


# ------------------------------- Flip ------------------------------- #
def flip():
    global is_front, e_word, word, language, card
    is_front = False
    canvas.itemconfig(word, text=e_word, fill="white")
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(card, image=card_back)


def front():
    global is_front, e_word, word, language, card
    is_front = True
    canvas.itemconfig(word, text=f_word, fill="black")
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(card, image=card_front)


def new_card():
    global duo, e_word, f_word, flip_timer
    window.after_cancel(flip_timer)
    duo = random.choice(data)
    f_word = duo[0]
    e_word = duo[1]
    front()
    flip_timer = window.after(3000, flip)


def right_click():
    new_card()


def wrong_click():
    global is_front
    if is_front:
        flip()
        window.after(3000, new_card)
    else:
        new_card()
# ------------------------------- UI ------------------------------ #

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

card_back = PhotoImage(file=r"C:\Users\hasan\Desktop\python\yeni\20) flashing_cards\images\card_back.png")
card_front = PhotoImage(file=r"C:\Users\hasan\Desktop\python\yeni\20) flashing_cards\images\card_front.png")
right = PhotoImage(file=r"C:\Users\hasan\Desktop\python\yeni\20) flashing_cards\images\right.png")
wrong = PhotoImage(file=r"C:\Users\hasan\Desktop\python\yeni\20) flashing_cards\images\wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card = canvas.create_image(0, 0, anchor=NW, image=card_front)
language = canvas.create_text(400, 158, text="French", font=("Arial", 20, "bold"))
word = canvas.create_text(400, 258, text=f_word, font=("Arial", 17, "normal"))

right_button = Button(image=right, highlightthickness=0, command=right_click)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong, highlightthickness=0, command=wrong_click)
wrong_button.grid(row=1, column=0)

flip_timer = window.after(3000, flip)

window.mainloop()
