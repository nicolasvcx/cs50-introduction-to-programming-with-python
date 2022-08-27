def main():

    fuel_amount = input("Amount of Fuel: ")
    percentage = convert(fuel_amount)
    gas = gauge(percentage)
    print(gas)

def convert(fraction):

    try:
        x,y = fraction.split("/")
        x = int(x)
        y = int(y)
        fraction = (x / y) * 100
        return int(fraction)
    except (ValueError, ZeroDivisionError):
        raise

def gauge(percentage):

    if (percentage > 100):
        main()
    elif (percentage <= 10 and percentage >= 0):
        return "E"
    elif (percentage == 25):
        return "25%"
    elif (percentage <= 55 and percentage >= 45):
        return "50%"
    elif (percentage == 75):
        return "75%"
    elif (percentage >= 95 and percentage <= 100 ):
        return "F"


if __name__ == "__main__":
    main()
