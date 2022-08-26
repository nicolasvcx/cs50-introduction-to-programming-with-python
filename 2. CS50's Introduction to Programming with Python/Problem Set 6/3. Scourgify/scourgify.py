import sys
import csv
import array

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
try:
    with open(sys.argv[2], "w") as create:
        header = "foo"
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(create, fieldnames=fieldnames)
        writer.writeheader()
        with open(sys.argv[1], "r") as before:
            reader = csv.DictReader(before)
            for row in reader:
                last_name, first_name = row['name'].split(", ")
                writer.writerow({'first': first_name, 'last': last_name, 'house': row['house']})
except FileNotFoundError:
    sys.exit("Could not find " + sys.argv[1])