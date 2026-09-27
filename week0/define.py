def main():
    hello()
    name = input("Name: ")
    hello(name)

def hello(to="world"):
    to = to.strip().capitalize()
    print(f"Hello, {to}")

main()

