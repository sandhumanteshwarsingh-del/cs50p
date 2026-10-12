import random


def main():
    correct = 0
    n = get_level()
    for _ in range(1, 11):
        x = generate_integer(n)
        y = generate_integer(n)
        counter = 1
        while True:
            print(f"{x} + {y} = ", end="")
            answer = int(input())
            if answer != x + y:
                if counter <=2:
                    print("EEE")
                    counter+=1
                elif counter > 3:
                    print(f"{x} + {y} = {x + y}")
                    break
            elif answer == x + y:
                correct+=1
                break
    print(correct)

def get_level():
    while True:
        tmp = int(input("Choose a level: "))
        if tmp != 1 and tmp != 2 and tmp != 3:
            continue
        else:
            break
    return tmp    

def generate_integer(level):
    if level == 1:
        tmp = random.randint(1, 9)
    elif level == 2:
        tmp = random.randint(10, 99)
    else:
        tmp = random.randint(100, 999)
    return tmp

if __name__ == "__main__":
    main()