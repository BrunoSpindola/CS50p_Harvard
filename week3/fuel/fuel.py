def main():
    while True:
        try:
            x, y = input("Fraction: ").split('/')
            x, y = int(x), int(y)
            if y <= 0 or x < 0 or x > y:
                continue
            print(get_percentage(x, y))
            break
        except (ValueError, ZeroDivisionError):
            pass

def get_percentage(x, y):
    percentage = (x / y) * 100

    if int(percentage) <= 1:
        return "E"
    elif int(percentage) >= 99:
        return "F"
    else:
        return f"{int(percentage)}%"

main()
