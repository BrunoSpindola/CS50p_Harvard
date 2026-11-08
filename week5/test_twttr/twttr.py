def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")

def shorten(word):

    # vowels = ['a', 'e', 'i', 'o', 'u']
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    result = ""
    for letter in word:
        if letter in vowels:
            result += ""
        else:
            result += letter

    return result

if __name__ == "__main__":
    main()
