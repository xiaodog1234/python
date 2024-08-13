userInput = input("Input: ")

for letter in userInput:
    if letter == "A" or letter == "a" or letter == "E" or letter == "e" or letter == "I" or letter == "i" or letter == "O" or letter == "o" or letter == "U" or letter == "u":
         userInput = userInput.replace(letter, "")
print("Output: ", userInput)
