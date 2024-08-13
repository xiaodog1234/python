def main():
    userInput = input()
    convert(userInput)

def convert(userInput):
    print(userInput.replace(":)", "🙂").replace(":(","🙁"))

main()
