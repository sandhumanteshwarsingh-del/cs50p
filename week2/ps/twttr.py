def main():
    text = input("Text: ")
    print(shorten(text))

def shorten(text):
    string = ""
    for word in text:
        if word.lower() == "a" or word.lower() == "e" or word.lower() == "i" or word.lower() == "o" or word.lower() == "u":
            word = ""
        string = string + word
    return string

main()
