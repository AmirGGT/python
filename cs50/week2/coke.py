coins = [5,10,25]
amount_due = 50
while amount_due > 0:
    print(f"Amount due: {amount_due}")
    payment = int(input("insert coin : "))
    if payment in coins:
        amount_due -= payment
    else:
        print("error!!try again")
print(f"\nchange owed: {abs(amount_due)}")
