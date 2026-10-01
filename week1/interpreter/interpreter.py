def main():
    a = input()
    print(interpret(a))

def interpret(a):
    x, operator, y = a.split()
    x = int(x)
    y = int(y)
    match operator:
        case "+":
            return x + y
        case "-":
            return x - y
        case "/":
            return x/y
        case "*":
            return x*y
        case "%":
            return x%y
        case _:
            return "Invalid Input"

main()
