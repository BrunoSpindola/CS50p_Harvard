import random

while True:
    try:
        n = int(input("Level: "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        pass

random_val = random.randint(1, n)

while True:
    try:
        guess_num = int(input("Guess: "))
        if guess_num <= 0:
            raise ValueError
    except ValueError:
        continue

    if guess_num == random_val:
        print("Just right!")
        break
    elif guess_num < random_val:
        print("Too small!")
    else:
        print("Too large!")

