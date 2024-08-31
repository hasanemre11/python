import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.bgpic("blank_states_img.gif")
screen.setup(width=720, height=500)

data = pandas.read_csv("50_states.csv")
data_dict = pandas.read_csv("50_states.csv")["state"].to_list()

states = data["state"].to_list()

print(data_dict)

on = True

while on:
    answer = screen.textinput(title="Guess a state", prompt="What is another state's name").title()
    if answer in states:
        data_1 = data[data.state == answer]
        print(data_1)
        x = data_1["x"].to_list()[0]-13
        y = data_1["y"].to_list()[0]
        state = Turtle()
        state.hideturtle()
        state.penup()
        state.goto(x, y)
        state.write(f"{answer}")
    if answer == "Exit":
        break
screen.mainloop()
