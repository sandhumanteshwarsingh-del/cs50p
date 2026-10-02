def main():
    fruit = input("Fruit: ")
    print(nutrition(fruit.lower()))

def nutrition(fruit):
    Fruits = {
        "apple": "130",
        "avocado": "50",
        "banana": "110",
        "cantaloupe": "50",
        "grapefruit": "60"
    }
    return Fruits[fruit]

main()