import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.goto(random.randint(-300, 300), random.randint(-300, 300))
        self.color("red")

    def eaten(self):
        self.clear()
        self.goto(random.randint(-300, 300), random.randint(-270, 270))
