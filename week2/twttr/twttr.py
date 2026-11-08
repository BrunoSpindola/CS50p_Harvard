string = input("Input: ")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

result = ""
for letter in string:
    if letter in vowels:
        result += ""
    else:
        result += letter

print(f"Output: {result}")
