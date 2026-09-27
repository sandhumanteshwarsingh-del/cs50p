c = 3 * pow(10, 8)

def main():
    mass = int(input("M: "))
    print(convert(mass))

def convert(m):
    return m*c*c

main()