import emoji

userInput = input("Input: ")

print(f"Output: {emoji.emojize(userInput, language='alias')}")
