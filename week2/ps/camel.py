def main():
    camel = input("camelCase: ")
    snake(camel)

def snake(text):
    print("snake_case: ", end="")
    for word in text:
        if word.isupper():
            word = "_" + word.lower()
        print(word, end="")
    print()
main()