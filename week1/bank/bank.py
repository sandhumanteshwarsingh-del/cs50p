def main():
    greet, name = input().lower().split()
    calculate(greet)

def calculate(greet):
    if ( greet == "hello"):
        print("$0")
    elif (greet[0] == "h"):
        print("$20")
    else:
        print("$100")

main()

