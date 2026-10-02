def main():
    owed = 50
    print("You owe 50 cents")
    while owed != 0:
        intake = get_input()
        owed = owed - intake
        print(f"You owe {owed}")
    print("Dues cleared")

def get_input():
    while True:
        intake = int(input("Insert a coin: "))
        if intake == 25 or intake == 10 or intake == 5:
            break
        else:
            continue
    return intake

main()