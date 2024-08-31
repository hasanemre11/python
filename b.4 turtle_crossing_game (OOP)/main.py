from turtle import Screen
import time
from cars import Cars
from player import Player
from score import Score

screen = Screen()
screen.setup(width=650, height=650)
screen.bgcolor("white")
screen.tracer(0)

cars = Cars()
player = Player()
score = Score()

on = True

while on:
    screen.update()
    time.sleep(0.1)
    player.move()
    cars.move()
    on = cars.collision(player)
    if not on:
        score.finish()
    if player.ycor() == 290:
        player.goto(0, -280)
        score.adding()
        cars.increase_speed()
















screen.exitonclick()