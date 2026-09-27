def main():
    x = int(input("What is x? "))
    y = int(input("What is y? "))
    compare(x, y)

def compare(x, y):
    if x > y:
        print("x is greater than y")
    elif y > x:
        print("x is less than y")
    else:
        print("They are equal")

main()