tacos = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def __main__():

    total_value = 0
    while True:
        try:
            item = input("Item: ").title()
            if item in tacos:
                total_value += tacos[item]
                print("Total: ${:.2f}".format(total_value))
        except (EOFError, KeyError):
            break

__main__()