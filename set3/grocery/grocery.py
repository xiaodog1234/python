def main():
    # groceryList = {
    #     "itemName": 0,
    #     "itemName": 0
    # }
    groceryList = {}
    while True:
        try:
            item = input()
        except EOFError:
            break
        else:
            #check if item is in the grocerylist
            if isInList(groceryList, item.upper()):
                number = int(groceryList[item.upper()]) + 1
                groceryList.update({item.upper(): number})
            else:
                groceryList[item.upper()] = 1
                #for i in groceryList:
                #    print(groceryList[i])

    for key,value in sorted(groceryList.items()):
        print("{} {}".format(value, key))

def isInList(groceryList, itemPass):
    if itemPass in groceryList:
        return True
    return False

main()
