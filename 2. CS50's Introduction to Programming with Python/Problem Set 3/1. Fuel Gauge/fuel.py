def gas(fuel):

    x = int(fuel.split("/")[0])
    y = int(fuel.split("/")[1])
    
    if (x / y > 1):
        __main__()
    elif (x / y <= 0.10 and x / y >= 0):
        print("E")
    elif (x / y == 0.25):
        print("75%")
    elif (x / y <= 0.55 and x / y >= 0.45):
        print("50%")
    elif (x / y == 0.75):
        print("75%")
    elif (x / y >= 0.95 and x / y <= 1 ):
        print("F")

def __main__():

    fuel_amount = input("Amount of Fuel: ")
    try:
        gas(fuel_amount)
    except (ValueError, ZeroDivisionError):
        __main__()

__main__()

