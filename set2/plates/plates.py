def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    firstNumber = True
    numberEncounter = False
    if " " in s or "." in s or "," in s:
        return False
    elif len(s) > 6 or len(s)<2:
        return False
    elif not isLetter(s[0]) and not isLetter(s[1]):
        return False
    for c in s:
        #number in middle check
        if isLetter(c):
            if numberEncounter == True:
                return False
        if isNumber(c):
            # check if firstNumber is 0
            if firstNumber == True and c =="0":
                return False
            else:
                firstNumber = False
            # check if this is the first time we encounter a number
            if numberEncounter == False:
                numberEncounter = True
            """
            #check if number is in the middle
            #print("s.rsplit(sep=c): ", s.rsplit(sep=c,maxsplit=-1)[1])
            if not allNumber(s.rsplit(sep=c,maxsplit=-1)[1]):
                return False
            else:
                return True
            """
    return True

def isLetter(c):
    return c.isalpha()

def isNumber(c):
    return c.isnumeric()

def allNumber(c):
    #print("allNumber: ", c)
    if len(c) > 0:
        for i in c:
            if not isNumber(i):
                return False
        return True
    return True
main()
