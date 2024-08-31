theme_color = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
import random
import time


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=theme_color)

        self.score = 0

        self.score_label = Label(text=f"Score: {self.score}", font=("Arial", 8, "normal"), bg=theme_color)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text=self.quiz.text_, font=("Arial", 12, "italic"), width=250)
        self.canvas.grid(row=1, column=0, columnspan=2)

        right = PhotoImage(file=r"C:\Users\hasan\Desktop\python\yeni\22) quiz_game\images\true.png")
        self.right_button = Button(image=right, highlightthickness=0, bg=theme_color, command=self.right_click)
        self.right_button.grid(row=2, column=0)

        wrong = PhotoImage(file=r"C:\Users\hasan\Desktop\python\yeni\22) quiz_game\images\false.png")
        self.wrong_button = Button(image=wrong, highlightthickness=0, bg=theme_color, command=self.wrong_click)
        self.wrong_button.grid(row=2, column=1)

        self.window.mainloop()

    def right_click(self):
        self.quiz.user_answer = "True"
        self.check_answer()

    def wrong_click(self):
        self.quiz.user_answer = "False"
        self.check_answer()

    def check_answer(self):
        if self.quiz.user_answer == self.quiz.answer_:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.quiz.question_number += 1
        self.window.after(3000, self.new)

    def new(self):
        self.quiz.question = self.quiz.question = random.choice(self.quiz.question_list)
        self.quiz.answer_ = self.quiz.question.answer
        self.quiz.text_ = self.quiz.question.text
        self.score_label.config(text=f"Score: {self.score}")
        self.canvas.itemconfig(self.question_text, text=self.quiz.text_)
        self.canvas.config(bg="white")
