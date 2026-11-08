grocery = {}

while True:
    try:
        item = input("").upper()
        grocery[item] = grocery.get(item, 0) + 1
    except EOFError:
        print()
        for item in sorted(grocery):
            print(f"{grocery[item]} {item}")
        break
