from logo import logo, vs
from data import data
import random



data = data
print(logo)
vs = vs

on = True
score = 0


while on:
    first = random.choice(data)
    second = random.choice(data)

    first_name = first["name"]
    first_follower_count = first["follower_count"]
    first_description = first["description"]
    first_country = first["country"]

    second_name = second["name"]
    second_follower_count = second["follower_count"]
    second_description = second["description"]
    second_country = second["country"]

    print(f"Compare A:{first_name}, a {first_description}, from {first_country}")
    print(vs)
    print(f"Against B:{second_name}, a {second_description}, from {second_country}")
    answer = input("Who has more followers? Type A or B: ")

    if (answer == "A" and first_follower_count > second_follower_count) or \
            (answer == "B" and first_follower_count < second_follower_count):
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Your final score is {score}")
        on = False