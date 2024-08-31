theme_color = "#375362"
from tkinter import *


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=theme_color)

        self.score = 0

        self.score_label = Label(text=f"Score: {self.score}", font=("Arial", 8, "normal"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question = self.canvas.create_text(150, 125, text="", font=("Arial", 8, "normal"))
        self.canvas.grid(row=1, column=1)

        right = PhotoImage(file=r"C:\Users\hasan\Desktop\python\yeni\20) flashing_cards\images\right.png")
        self.right_button = Button(image=right, highlightthickness=0)
        self.right_button.grid(row=2, column=0)

        wrong = PhotoImage(file=r"C:\Users\hasan\Desktop\python\yeni\20) flashing_cards\images\wrong.png")
        self.wrong_button = Button(image=wrong, highlightthickness=0)
        self.wrong_button.grid(row=2, column=1)

        self.window.mainloop()
