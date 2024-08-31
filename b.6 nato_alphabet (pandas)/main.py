import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data)
alp = data.letter.to_dict()

alphabet = {value: data.code.to_dict()[key] for (key, value) in alp.items()}
print(alphabet)


while True:
    try:
        word = input("Enter the word: ").upper()
        result = [alphabet[letter] for letter in word]
        print(result)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")

