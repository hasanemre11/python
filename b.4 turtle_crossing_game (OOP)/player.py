from turtle import Turtle, Screen


class Player(Turtle):

    def __init__(self):
        self.screen = Screen()
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(0, -280)
        self.setheading(90)

    def up(self):
        self.forward(10)

    def move(self):
        self.screen.listen()
        self.screen.onkey(self.up, "Up")
