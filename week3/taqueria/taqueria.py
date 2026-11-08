def main():
    total = 0
    while True:
        try:
            client_item = input("Item: ").title()
            value = taqueria_items(client_item)
            if value == 0:
                continue
            total += value
            print(f"Total: ${total:.2f}")
        except EOFError:
            print()
            break

def taqueria_items(item):
    menu = {
            "Baja Taco": 4.25,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
             }

    if item in menu:
        return menu[item]
    else:
        return 0

main()
