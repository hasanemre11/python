import random
from turtle import Turtle, Screen
from tahta import Tahta
import time
from scoreboard import Scoreboard
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=900, height=600)
screen.tracer(0)

scoreboard = Scoreboard()

ball = Ball()

tahta_1 = Tahta(420)
tahta_2 = Tahta(-420)

on = True
ball.move()

while on:
    screen.update()
    time.sleep(0.1)
    ball.forward(15)
    tahta_1.move("Up", "Down")
    tahta_2.move("w", "s")
    ball.wall_collision()
    if 410 > ball.xcor() > 390 and ball.distance(tahta_1) < 60:
        if ball.heading() == 330:
            ball.setheading(210)
        elif ball.heading() == 30:
            ball.setheading(150)
    if ball.xcor() < -395 and ball.distance(tahta_2) < 60:
        if ball.heading() == 150:
            ball.setheading(30)
        elif ball.heading() == 210:
            ball.setheading(150)
    if -485 < ball.xcor() < -475:
        scoreboard.score1()
    if 485 > ball.xcor() > 475:
        scoreboard.score2()
    if ball.xcor() > 600 or ball.xcor() < -600:
        ball.home()
        ball.setheading(random.choice([30, 150, 210, 330]))
screen.exitonclick()
