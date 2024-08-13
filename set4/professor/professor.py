import random


def main():
    level = get_level()
    problemLeft = 10
    score = 0
    while problemLeft > 0:
        totalAttempt = 3
        try:
            x = generate_integer(level)
            y = generate_integer(level)
        except:
            pass
        else:
            while totalAttempt > 0:
                try:
                    userAnswer = int(input(f"{x} + {y} ="))
                except:
                    totalAttempt = totalAttempt - 1
                    pass
                else:
                    if userAnswer == (x+y):
                        score = score + 1
                        break
                    else:
                        totalAttempt = totalAttempt - 1
                        print("EEE")
            if totalAttempt == 0:
                print(f"{x} + {y} = {x+y}")
            problemLeft = problemLeft - 1

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            userLevel = int(input("Level: "))
        except:
            pass
        else:
            if(userLevel <=3 and userLevel >=1):
                return userLevel

def generate_integer(level):
    if level != 1 and level != 2 and level != 3:
        raise ValueError
    elif level == 1:
        return random.randint(0,9)
    elif level ==2:
        return random.randint(10,99)
    elif level ==3:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
