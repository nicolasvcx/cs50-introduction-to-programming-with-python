import sys
from tkinter import font
from pyfiglet import Figlet

figlet = Figlet()
font_list = figlet.getFonts()

if sys.argv[1] != "-f" and sys.argv[1] != "--font":
    sys.exit("Invalid usage")
elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
    if sys.argv[2] in font_list:
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")


string = input("Input: ")
print()
print(figlet.renderText(string))
