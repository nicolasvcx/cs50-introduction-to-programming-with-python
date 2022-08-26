string = input("Expression: ")

x, y, z = string.split(" ")

if (y == "+"):
    print(float(int(x) + int(z)))
elif (y == "-"):
    print(float(int(x) - int(z)))
elif (y == "*"):
    print(float(int(x) * int(z)))
elif (y == "/"):
    print(int(x) / int(z))
