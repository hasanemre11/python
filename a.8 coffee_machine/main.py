MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def coin():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def make(cof):
    global profit
    resources['water'] += -MENU[cof]["ingredients"]["water"]
    if cof != "espresso":
        resources['milk'] += -MENU[cof]["ingredients"]["milk"]
    resources['coffee'] += -MENU[cof]["ingredients"]["coffee"]
    profit += MENU[cof]["cost"]
    print(f"Here is your {coffee} ☕️. Enjoy!")


def check_resources(cof):
    enough = True
    if resources['water'] < MENU[cof]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        enough = False
    if cof != "espresso":
        if resources['milk'] < MENU[cof]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            enough = True
    if resources['coffee'] < MENU[cof]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        enough = True
    return enough


on = True

while on:
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee == "report":
        report()
    elif coffee == "latte" or coffee == "espresso" or coffee == "cappuccino":
        total = coin()
        if total < MENU[coffee]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        elif check_resources(coffee):
            print(f"Here is ${total-MENU[coffee]['cost']} in change")
            make(coffee)

