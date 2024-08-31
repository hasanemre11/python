from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(250, 270)
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Arial", 19, "normal"))

    def adding(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 19, "normal"))

    def finish(self):
        self.home()
        self.write(f"GAME OVER", align="center", font=("Arial", 20, "normal"))