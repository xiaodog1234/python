from pyfiglet import Figlet
import random
import sys

def main(fontType):
    figlet = Figlet()
    userInput = input("Input: ")
    if fontType =="random":
        fontChoice = random.choice(figlet.getFonts())
        figlet.setFont(font=fontChoice)
    else:
        figlet.setFont(font=fontType)
    print("Output:")
    print(figlet.renderText(userInput))

#name of file in command line count as one argument
figlet = Figlet()
if len(sys.argv) > 3:
    sys.exit("Invalid usage")
elif len(sys.argv)==2:
    sys.exit("Invalid usage")
else:
    if len(sys.argv) == 1:
        main("random")
    else:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if not sys.argv[2] in figlet.getFonts():
                sys.exit("Invalid usage")
            main(sys.argv[2])
        else:
            sys.exit("Invalid usage")


