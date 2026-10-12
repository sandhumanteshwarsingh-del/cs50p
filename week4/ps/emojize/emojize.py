import emoji

def main():
    x = input("Input: ")
    output = emojize(x)
    print(output)

def emojize(raw):
    return emoji.emojize(raw, language="alias")

main()