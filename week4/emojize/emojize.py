import emoji

str_emoji = input("Input: ")

print(f"Output: {emoji.emojize(str_emoji, language='alias')}")
