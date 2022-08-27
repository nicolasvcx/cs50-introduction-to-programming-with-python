import random

while True:
    try:
        level = int(input("Level: "))
        if (level > 0) and (level < 101):
            break
    except:
        pass

answer = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if (guess > 0):
            if (guess < answer):
                print("Too Small!")
            elif (guess > answer):
                print("Too Large!")
            else:
                 print("Just Right!")
                 break
    except:
        pass