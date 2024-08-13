nameList = []
while True:
    try:
        nameList.append(input("Name: "))
    except EOFError:
        break
printString = "Adieu, adieu, to "
if len(nameList) == 1:
    printString = printString + nameList[0]
elif len(nameList) ==2:
    printString = printString + nameList[0] + " and " + nameList[1]
elif len(nameList) > 2:
    for name in nameList:
        if nameList.index(name) == 0:
            printString = printString + name
        elif nameList.index(name) == len(nameList) - 1:
            printString = printString + ", and " + name
        else:
            printString = printString + ", " + name
print(printString)
