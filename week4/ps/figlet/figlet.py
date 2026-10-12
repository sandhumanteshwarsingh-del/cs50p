import pyfiglet
import sys
import random

if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid Usage")

if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid Usage")

def main():
    text = input()
    print(convert(text))

def convert(text):
    if len(sys.argv) == 3:
        try:
            output = pyfiglet.figlet_format(text, font=sys.argv[2])
        except pyfiglet.FontNotFound:
            sys.exit("Invalid Font")
    elif len(sys.argv) == 1:
        font_random = random.choice(pyfiglet.FigletFont.getFonts())
        output = pyfiglet.figlet_format(text, font=font_random)
    return output

if __name__ == "__main__":
    main()