def main():
    text = input("Text: ")
    print(shorten(text))

def shorten(text):
    string = ""
    for word in text:
        if word.lower() in "aeiou":
            word = ""
        string = string + word
    return string

main()
