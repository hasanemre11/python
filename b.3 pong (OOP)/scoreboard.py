from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 200)
        self.color("white")
        self.score_1 = 0
        self.score_2 = 0
        self.write(f"{self.score_1}    {self.score_2}", align="center", font=("Arial", 50, "normal"))

    def score1(self):
        self.score_1 += 1
        print(self.score_1, self.score_2)
        self.clear()
        self.write(f"{self.score_1}    {self.score_2}", align="center", font=("Arial", 50, "normal"))

    def score2(self):
        self.score_2 += 1
        print(self.score_1, self.score_2)
        self.clear()
        self.write(f"{self.score_1}    {self.score_2}", align="center", font=("Arial", 50, "normal"))