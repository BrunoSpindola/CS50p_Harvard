import csv
import sys
import os

if len(sys.argv) == 1:
    sys.exit("Too few command-line argument")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line argument")

else:
    try:
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]

        if not os.path.exists(filename1) or not filename1.endswith(".csv") or not filename2.endswith(".csv"):
            raise FileNotFoundError

        with open(filename1, "r") as file1, open(filename2, "w", newline="") as file2:
            reader = csv.DictReader(file1)
            writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({"first": first, "last": last, "house": row["house"]})

    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")
