import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # [0-9] checks for number between 0 and 9
    # + is a quantifier for 1 or more
    # \. for the "."
    # $ End of line or pattern
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        # Put numbers in a list
        number_list = ip.split(".")
        # Iterate through each of them and check if they are bigger than 0 and smaller than 255
        for number in number_list:
            if int(number) < 0 or int(number) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()