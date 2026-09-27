def hello(to="world"):
    to = to.strip().capitalize()
    print(f"Hello, {to}")

hello()
name = input("Name: ")
hello(name)