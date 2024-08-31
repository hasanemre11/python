alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo

print(logo)


def caesar(direction):
    w = input("Type your massage:")
    num = int(input("Type the shift number: "))
    print("Here's the result: ", end="")
    for i in w:
        if i in alphabet:
            index = alphabet.index(i)

            if direction == "encode":
                print(alphabet[index + num], end="")
            elif direction == "decode":
                print(alphabet[index - num], end="")


on = True

while on:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    caesar(choice)
    print("")
    conti = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    if conti == "no":
        print("Goodbye!")




