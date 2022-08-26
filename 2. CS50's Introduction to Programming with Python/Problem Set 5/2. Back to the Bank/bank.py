def main():
    greeting = input("Input: ")
    string = value(greeting)
    print(f"${string}")

def value(greeting):
    greeting = greeting.replace(" ", "")
    if (greeting.lower() == "hello"):
        return 0
    elif (greeting[0].lower() == "h"):
        return 20
    elif (greeting.isalpha() == False):
        main()
    else:
        return 100

if __name__ == "__main__":
    main()
