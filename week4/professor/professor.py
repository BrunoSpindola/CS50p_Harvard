import random


def main():
    score = 0
    level = get_level()

    for i in range(0, 10):
        error = 0
        x = generate_integer(level)
        y = generate_integer(level)
        result = get_result(x, y)

        if result != (x + y):
            print("EEE")
            error += 1

            while result != (x + y) and error < 3:
                result = get_result(x, y)

                if result != (x + y):
                    print("EEE")
                    error += 1

                else:
                    score += 1

            if error == 3:
                print(f"{x} + {y} = {x + y}")
        else:
            score += 1

    print(f"Score: {score}")

def get_level():
    levels = [1, 2, 3]
    try:
        level = int(input("Level: "))
        if level not in levels:
            raise ValueError

    except ValueError:
        return get_level()

    return level

def get_result(x, y):
    try:
        return int(input(f"{x} + {y} = "))
    except ValueError:
        return None

def generate_integer(level):
    if level == 1:
        integer = random.randint(0, 9)
    elif level == 2:
        integer = random.randint(10, 99)
    else:
        integer = random.randint(100, 999)

    return integer

if __name__ == "__main__":
    main()
