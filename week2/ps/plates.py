def main():
    plate_number = input("PLATE: ")
    if is_valid(plate_number):
        print("Valid")
    else:
        print("Not valid")

def is_valid(text):
    iteration = 1
    flag = 0
    for letter in text:
        if letter in ". !":
            return False
        if iteration == 1 or iteration == 2:
            if not letter.isalpha():
                return False
        if not letter.isalpha():
            flag = 1
        if flag == 1 and letter.isalpha():
            return False
        iteration = iteration + 1
    if not 2 <= len(text) <= 6:
        return False
    return True

main()