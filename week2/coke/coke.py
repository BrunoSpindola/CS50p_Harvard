def main():
    amount = 50

    while amount > 0:
        print(f"Amount Due: {amount}")
        coin = int(input("Insert Coin: "))

        if coin in (25, 10, 5):
            if coin > amount:
                print(f"Change Owed: {coin - amount}")
                amount = 0
            else:
                amount -= coin

    print("Change Owed: 0")

if __name__ == "__main__":
    main()
