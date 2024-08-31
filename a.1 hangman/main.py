import random
import words
import stages

print(stages.logo)

chosen = random.choice(words.word_list)
print(chosen)
end = False
lives = 6

d = []
v = []
for letter in chosen:
    d.append("_")
    v.append(letter)


def printing_d():
    for i in d:
        print(i, "", end="")


def arranging_d(a):
    count = -1
    for i in chosen:
        count += 1
        if a == i:
            d[count] = a


while not end:
    print("")
    guess = input("Guess a letter:")
    if guess in chosen:
        arranging_d(guess)
        print(stages.stages[lives])
        printing_d()
        if d == v:
            print("You won!")
            end = True

    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives += -1
        print(stages.stages[lives])
        printing_d()
        if lives == 0:
            end = True
            print("You lose!")
