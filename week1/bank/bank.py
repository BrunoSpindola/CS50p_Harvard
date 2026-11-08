greet = input("Greeting: ").lower()
match greet:
    case greet if greet == 'hello':
        print("$0")
    case greet if greet.startswith("h") and greet != 'hello':
        print("$20")
    case _:
        print("$100")
