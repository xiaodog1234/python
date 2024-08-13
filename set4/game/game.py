import random

while True:
    try:
        numberRange = int(input("Level: "))
    except:
        pass
    else:
        if isinstance(numberRange, int) and numberRange >0:
            break
number = random.randint(1,numberRange)
#print(number)
while True:
    try:
        user_guess = int(input("Guess: "))
    except:
        pass
    else:
        if user_guess == number:
            print("Just right!")
            break
        elif user_guess > number:
            print("Too large!")
        elif user_guess < number and user_guess >=0:
            print("Too small!")
