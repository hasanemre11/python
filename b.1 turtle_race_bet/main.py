import random
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=500)

bet = screen.textinput(title="Make your bet!", prompt="Which one will win? Enter a color: ")

black = Turtle()
yellow = Turtle()
blue = Turtle()
green = Turtle()
red = Turtle()

turtles = [black, yellow, blue, green, red]
colors = ["black", "yellow", "blue", "green", "red"]
number = -1
y = 200
for turtle in turtles:
    number += 1
    turtle.color(colors[number])
    turtle.penup()
    turtle.shape("turtle")
    turtle.goto(x=-250, y=y)
    y -= 100


def move(t):
    m = random.randint(1, 10)
    t.forward(m)


def winner(l):
    w = ""
    xcor = -300
    for tu in l:
        if tu.xcor() > xcor:
            w = tu
            xcor = tu.xcor()
    return w


not_over = True

wi = winner(turtles)

while not_over:
    for t in turtles:
        move(t)
    wi = winner(turtles)
    if wi.xcor() > 250:
        not_over = False


if bet == wi.color()[0]:
    print(f"You won the bet! Winner is {wi.color()[0]}!")
else:
    print(f"You lost the bet! Winner is {wi.color()[0]}!")


screen.exitonclick()
