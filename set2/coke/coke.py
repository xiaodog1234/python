amount_due = 50
while amount_due > 0:
    print("Amount Due:", amount_due)
    insert_amount = int(input("Insert Coin: "))
    if insert_amount == 5 or insert_amount == 10 or insert_amount == 25:
        amount_due = amount_due - insert_amount

print("Change Owed:", amount_due*-1)
