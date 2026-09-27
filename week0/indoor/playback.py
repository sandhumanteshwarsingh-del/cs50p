def main():
    text = input("Speak: ")
    print(slow(text))

def slow(s):
    return s.replace(" ", "...")

main()
