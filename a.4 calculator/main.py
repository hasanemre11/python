from logo import logo

print(logo)



on = True
first_number = float(input("What is first number?: "))

while on:
    result = 0
    print("+")
    print("-")
    print("*")
    print("/")
    op = input("Pick an operation:")
    second_number = float(input("What is next number?: "))

    if op == "+":
        result = first_number + second_number
    elif op == "-":
        result = first_number - second_number
    elif op == "*":
        result = first_number * second_number
    elif op == "/":
        result = first_number / second_number
    print(f"{first_number} {op} {second_number} = {result}")
    c = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
    if c == "y":
        first_number = result
    elif c == "n":
        first_number = float(input("What is first number?: "))


