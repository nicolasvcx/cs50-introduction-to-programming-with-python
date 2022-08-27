import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

        time = re.search(r"^([0-9]+):?([0-9]+)? (A?P?M) to ([0-9]+)?:?([0-9]+)? (A?P?M)$", s, re.IGNORECASE)

        if int(time.group(1)) > 12 or int(time.group(4)) > 12:
            raise ValueError
        if int(time.group(2)) > 60 or int(time.group(6)) > 60:
            raise ValueError
        if time.group(3) != 'am' or time.group(3) != 'AM' or time.group(3) != 'PM' or time.group(3) != 'pm':
            raise ValueError


if __name__ == "__main__":
    main()
