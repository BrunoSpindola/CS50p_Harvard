from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[2] not in fonts:
        sys.exit("Invalid usage")

    elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font":
        figlet = Figlet(font=sys.argv[2])
        s = input("Input: ")
        print(f"Output:\n {figlet.renderText(s)}")
    else:
        sys.exit("Invalid usage")


elif len(sys.argv) == 1:
        f = random.choice(fonts)
        set_font = figlet.setFont(font=f)
        s = input("Input: ")
        print(f"Output:\n {figlet.renderText(s)}")
else:
    sys.exit("Invalid usage")
