def main():
    while True:
        try:
            percent = convert(input("Fraction: "))
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            print(f"{gauge(percent)}")
            break

def convert(fraction):
    userInput = fraction.split("/")
    try:
        percent = int(userInput[0])/int(userInput[1])
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError
    else:
        if int(userInput[0]) > int(userInput[1]):
            raise ValueError
        #print(f"percent: {percent*100}")
        return percent*100

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"

if __name__ == "__main__":
    main()

#print(f"{output*100:.0f}%")



