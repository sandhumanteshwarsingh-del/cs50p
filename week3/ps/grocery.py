def main():
    grocery_list = {}
    while True:
        try:
            item = input("Item: ").lower()
        except EOFError:
            print()
            break
        else:
            if item in grocery_list:
                grocery_list[item]+=1
            else:
                grocery_list[item] = 1

    sorted_dict = dict(sorted(grocery_list.items()))
    for item in sorted_dict:
        print(f"{sorted_dict[item]}: {item.upper()}")
main()