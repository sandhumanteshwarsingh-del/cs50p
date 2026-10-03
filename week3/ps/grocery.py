def main():
    grocery_list = {}
    while True:
        try:
            item = input("Item: ")
        except EOFError:
            print()
            break
        else:
            if item in grocery_list:
                grocery_list[item]+=1
            else:
                grocery_list[item] = 1
    for item in grocery_list:
        print(f"{grocery_list[item]}: {item}")
main()