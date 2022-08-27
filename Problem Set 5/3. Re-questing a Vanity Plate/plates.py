def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    position = 0
    final = len(s)
    first_digit = 0.1

    for i in s:
        if i in ("!","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~","."):
            return False

    if s[0:2].isnumeric():
        return False

    elif len(s) > 6 or len(s) < 2:
        return False

    for i in s:
        if i.isnumeric():
            first_digit = i
            for j in range(position, final):
                if s[j].isalpha() or first_digit == "0":
                    return False
        if first_digit == 0.1:
            position += 1
        else:
            break
    return True

if __name__ == "__main__":
    main()
