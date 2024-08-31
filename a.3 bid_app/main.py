from logo import logo
import os

print(logo)


on = True

name_and_bids = {}

while on:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    name_and_bids[name] = bid
    c = input("Are there any other bidders? Type yes or no: ")
    if c == "no":
        on = False

winner = ""
winner_bid = 0
for name in name_and_bids:
    if name_and_bids[name] > winner_bid:
        winner = name
        winner_bid = name_and_bids[name]
    elif name_and_bids[name] == winner_bid:
        winner = winner + "and" + name

print(f"The winner is {winner} with a bid of ${winner_bid}")


on = True

while on:
    print("1")





