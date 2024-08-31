import random
from turtle import Turtle


class Cars:
    def __init__(self):
        self.cars = []
        for i in range(1, 31):
            car = Turtle()
            self.speed = 10
            car.shape("square")
            car.shapesize(1, 2)
            car.penup()
            x = random.choice(range(-38, 38))
            y = random.choice(range(-62, 62))
            car.goto(10 * x, 4 * y)
            car.setheading(180)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor() < -400:
                car.goto(400, 4 * random.choice(range(-62, 62)))

    def collision(self, turtle):
        for car in self.cars:
            if -19 < car.ycor()-turtle.ycor() < 19 and -21 < car.xcor()-turtle.xcor() < 21:
                return False
        return True

    def increase_speed(self):
        self.speed += 5