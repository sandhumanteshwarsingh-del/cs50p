import random

def main():
    while True:
        level = int(input("Choose a level: "))
        if level <= 0:
            continue
        else: 
            break

    n = random.randint(1, level)
    while True:
        guess = int(input("Take a guess: "))
        if guess < n:
            print("Too low")
            continue
        elif guess > n:
            print("Too high")
        else:
            print("Just Right")
            return 0

main()
        
