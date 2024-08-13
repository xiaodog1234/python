def main():
    userInput = input("Input: ")
    print("Output:", shorten(userInput))

def shorten(word):
    for letter in word:
        if letter == "A" or letter == "a" or letter == "E" or letter == "e" or letter == "I" or letter == "i" or letter == "O" or letter == "o" or letter == "U" or letter == "u":
        #if letter in ["a","e","i","o","u"]
            word = word.replace(letter, "")
    return word


if __name__ == "__main__":
    main()
