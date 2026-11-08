def main():
    str_input = input("camelCase: ")
    snake_case = camelCase(str_input)
    print(f"snake_case: {snake_case}")

def camelCase(s):
    result = ""
    for letter in s:
        if letter.isupper():
            result += f"_{letter.lower()}"
        else:
            result += letter
    return result

if __name__ == "__main__":
    main()
