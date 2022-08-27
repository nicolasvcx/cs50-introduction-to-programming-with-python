import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search('(".+?")', s):
        string = re.search('(".+?")', s)
        url = string.group(1)
        try:
            first, second = url.split("/embed/")
            return "https://youtu.be/" + second[:-1]
        except ValueError:
            return
if __name__ == "__main__":
    main()