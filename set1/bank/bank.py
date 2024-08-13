userInput = input("Greeting: ").lower()

if "hello" in userInput:
    print("$0")
elif userInput[0] == "h":
    print("$20")
else:
    print("$100")
