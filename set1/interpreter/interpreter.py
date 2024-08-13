userInput = input("Expression: ").split(" ")
x = int(userInput[0])
y = userInput[1]
z = int(userInput[2])

match y:
    case "+":
        #print(round(float(x + z),1))
        print('{:.1f}'.format(int(x) + int(z)))
    case "-":
        print(round(float(x - z),1))
    case "*":
        print(round(float(x * z),1))
    case "/":
        print(round(float(x / z),1))
