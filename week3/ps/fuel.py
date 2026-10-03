while True:
    try:
        ratio = input("Insert a fraction x/y: ")
        nmtr, denom = ratio.split("/")
        nmtr = int(nmtr)
        denom = int(denom)

    except ValueError:
        pass

    else:
        if nmtr > denom:
                continue
        break

while True:
    try:
        ratio = nmtr/denom

    except ZeroDivisionError:
        pass

    else:
        break

if ratio >= 0.99:
    print("F")
elif ratio <= 0.01:
    print("E") 
else:
    percentage = round(ratio*100)
    print(f"{percentage}% fuel remains")
