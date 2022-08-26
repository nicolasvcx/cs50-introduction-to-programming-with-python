change_owed = 50

print()
while change_owed > 0:
    print("Amount Due: ", change_owed)
    coin = int(input("Insert Coin: "))
    if (coin == 25 or coin == 10 or coin == 5):
        change_owed -= coin
    else:
        print("Invalid Coin")

print("Change Owed: ", abs(change_owed))