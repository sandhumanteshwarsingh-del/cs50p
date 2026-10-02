def main():
    n = int(input("Height of box: "))
    print_box(n)

def print_box(side):
    for _ in range(side):
        print("#" * side)

main()