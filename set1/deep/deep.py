userInput = input("What is the Answer to the Great Question of Live, the Universe, and Everything? ")
userInput = userInput.lower().strip()
match userInput:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
