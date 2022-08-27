import inflect

p = inflect.engine()

names = []

def __main__():
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            list = p.join(names)
            print("\nAdieu, adieu, to " + list)
            break

__main__()


