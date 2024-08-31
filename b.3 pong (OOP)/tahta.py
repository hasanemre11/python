from turtle import Turtle, Screen


class Tahta(Turtle):

    def __init__(self, x):
        super().__init__()
        self.screen = Screen()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(1, 5)
        self.goto(x, 10)
        self.setheading(90)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 15)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 15)

    def move(self, up, down):
        self.screen.listen()
        if self.ycor() < 200:
            self.screen.onkey(self.up, up)
        if self.ycor() > -200:
            self.screen.onkey(self.down, down)
