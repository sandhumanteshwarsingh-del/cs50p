import inflect

def main():
    names = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            print()
            break
    adieu(names)

def adieu(names):
    p = inflect.engine()
    say_to = p.join(names)
    print(f"Adieu, adieu to {say_to}")
    
if __name__ == "__main__":
    main()
