string = input("Input")
string = string.replace(" ", "")
if (string[0].lower() == "h" and string[1].lower() == "e" and string[2].lower() == "l" and string[3].lower() == "l" and string[4].lower() == "o"):
    print("$0")
elif (string[0].lower() == "h"):
    print("$20")
else:
    print("$100")