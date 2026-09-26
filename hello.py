#take input from the user
name = input("What's your name? ").strip().title()

first, last = name.split()

#print the name of the user
print(f"hello, {first}")