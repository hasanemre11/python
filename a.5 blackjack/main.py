from logo import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)

user_cards = []
computer_cards = []


def card(who):
    first = random.choice(cards)
    second = random.choice(cards)
    while first == 11 and second == 11:
        first = random.choice(cards)
        second = random.choice(cards)
    who.append(first)
    who.append(second)


def calculate_score(who):
    score = 0
    for c in who:
        score += c

    return score


def take_card(who):
    who.append(random.choice(cards))


on = True

while on:
    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if answer == "y":
        card(user_cards)
        card(computer_cards)

        user_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score:{user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        comp_score = calculate_score(computer_cards)
        while comp_score < 14:
            take_card(computer_cards)
            comp_score = calculate_score(computer_cards)

        answer2 = input("Type 'y' to get another card, type 'n' to pass: ")

        while (user_score < 22) and answer2 == "y":
            take_card(user_cards)
            user_score = calculate_score(user_cards)
            if user_score < 22:
                print(f"Your cards: {user_cards}, current score:{user_score}")
                answer2 = input("Type 'y' to get another card, type 'n' to pass: ")

        print(f"Your cards: {user_cards}, final score:{user_score}")
        print(f"Computer's final hand: {computer_cards}, final score:{comp_score}")

        if user_score > 21:
            print("You went over!")
        elif user_score < 22 and 22 > comp_score > user_score:
            print("You lose!")
        elif user_score == comp_score:
            print("Draw!")
        else:
            print("You win!")
        computer_cards.clear()
        user_cards.clear()

    elif answer == "no":
        on = False