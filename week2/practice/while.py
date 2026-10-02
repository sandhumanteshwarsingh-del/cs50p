def main():
    n = input()
    meow(n)

def meow(n):
    n = int(n)
    while n > 0:
        print("Meow")
        n = n - 1

main()