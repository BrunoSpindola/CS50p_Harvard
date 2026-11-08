import sys
import os

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    try:
        count = 0
        filename = sys.argv[1]

        if not os.path.exists(filename) or not filename.endswith(".py"):
            raise FileNotFoundError

        with open(filename, "r") as file:
            for line in file:
                stripped = line.lstrip()
                if stripped.strip() and not stripped.startswith("#"):
                    count += 1

        print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")
