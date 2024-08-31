import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(1)
        self.penup()
        self.hh = random.randint(1, 4)

    def wall_collision(self):
        if self.heading() == 30 and 300 > self.ycor() > 290:
            self.setheading(330)
        if self.heading() == 150 and 300 > self.ycor() > 290:
            self.setheading(210)
        if self.heading() == 210 and -300 < self.ycor() < -290:
            self.setheading(150)
        if self.heading() == 330 and -300 < self.ycor() < -290:
            self.setheading(30)

    def move(self):
        if self.hh == 1:
            self.setheading(30)
        if self.hh == 2:
            self.setheading(150)
        if self.hh == 3:
            self.setheading(210)
        if self.hh == 4:
            self.setheading(330)

