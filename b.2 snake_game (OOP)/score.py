from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        file = open("score.txt")
        self.highscore = int(file.read())
        self.write(f"Score:{self.score}   High Score:{self.highscore}", align="center", font=("Arial", 24, "normal"))

    def add(self):
        self.clear()
        self.score += 1
        self.write(f"Score:{self.score}   High Score:{self.highscore}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            data = open("score.txt", "w")
            data.write(str(self.highscore))
        self.clear()
        self.score = 0
        self.write(f"Score:{self.score}   High Score:{self.highscore}", align="center", font=("Arial", 24, "normal"))