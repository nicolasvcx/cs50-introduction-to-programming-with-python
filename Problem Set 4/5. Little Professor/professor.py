import random


def main():
    points = 0

    level = get_level()
    for i in range(0, 10):
        x = generate_integer(level)
        y = generate_integer(level)
        errors = 0
        while errors < 3:
            try:
                print(x, "+", y , "= ", end="")
                user_answer = input()
                if int(user_answer) != (x + y):
                    errors += 1
                    print("EEE")
                elif int(user_answer) == (x + y):
                    errors = 0
                    points += 1
                    break
            except ValueError:
                errors += 1
                print("EEE")
        if errors == 3:
            print(x+y)
    print("Score: ", points)


def get_level():

    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass

    return level



def generate_integer(level):

    if level == 1:
        integer = random.randint(0, 9)
    elif level == 2:
        integer = random.randint(10, 99)
    else:
        integer = random.randint(100, 999)
    return integer


if __name__ == "__main__":
    main()
