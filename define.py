def hello(name):
    name = name.strip().capitalize()
    print(f"Hello, {name}")

name = input("Name: ")
hello(name)