import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=630, height=630)
screen.tracer(0)


score = Score()

food = Food()
snake = Snake()

on = True

while on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.eaten()
        score.add()
        snake.adding()
    if snake.collision():
        on = False
        score.reset()


screen.exitonclick()
