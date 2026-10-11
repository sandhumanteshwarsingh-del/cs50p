from random import shuffle
def main():
    x = ["Harry", "Hermione", "Ron", "Draco", "Manteshvar"]
    shuffle(x)
    for name in x:
        print(name, end=' ')
    print()
main()