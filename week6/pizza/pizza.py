import sys
import os
import csv
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    try:
        menu = []
        filename = sys.argv[1]

        if not os.path.exists(filename) or not filename.endswith(".csv"):
            raise FileNotFoundError

        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)

        headers = menu[0]
        print(tabulate(menu[1:], headers, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("Not a CSV file")
