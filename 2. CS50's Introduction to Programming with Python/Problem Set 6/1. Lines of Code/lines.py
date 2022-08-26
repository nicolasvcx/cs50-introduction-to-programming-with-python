import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
try:
    with open(sys.argv[1], "r") as file:
        i = 0
        for line in file:
            if not line.lstrip().startswith("#") and line.lstrip() != "":
                i += 1
        print(i)
except FileNotFoundError:
    sys.exit("File does not exist")