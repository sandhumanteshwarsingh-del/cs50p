def main():
    prompt = input("Answer to the Great Question of Life, the Universe and Everything? ")
    if (check(prompt)):
        print("Correct")
    else:
        print("Not correct")


def check(prompt):
    prompt = prompt.strip().lower()
    match prompt:
        case "forty-two": return True
        case "forty two": return True
        case "42": return True
        case _: return False

main()
    