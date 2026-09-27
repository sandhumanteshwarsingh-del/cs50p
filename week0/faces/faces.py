def main():
    text = input()
    print(convert(text))

def convert(original):
    return original.replace(":)", "🙂").replace(":(", "🙁")

main()