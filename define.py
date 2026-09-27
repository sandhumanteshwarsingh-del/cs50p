def hello(to):
    to = to.strip().capitalize()
    print(f"Hello, {to}")

name = input("Name: ")
hello(name)