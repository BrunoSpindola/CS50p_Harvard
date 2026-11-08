def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")

def value(greeting):
    greeting = greeting.strip().lower()
    
    match greeting:
        case greeting if greeting.startswith("hello"):
            return 0

        case greeting if greeting.startswith("h"):
            return 20

        case _:
            return 100

if __name__ == "__main__":
    main()
