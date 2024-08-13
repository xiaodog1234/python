while True:
    userInput = input("Fraction: ").split("/")
    try:
        output = int(userInput[0])/int(userInput[1])
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        if output > 1:
            continue
        elif output >= 0.99:
            print("F")
            break
        elif output <=0.01:
            print("E")
            break
        else:
            print(f"{output*100:.0f}%")
            break
