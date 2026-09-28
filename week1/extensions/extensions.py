def main():
    file = input("File name: ")
    print(filetype(file))

def filetype(name):
    fname, extn = name.lower().split(".", -1)
    match extn:
        case "txt":
            type_is = "Text File"
        case "jpg" | "jpeg" | "png":
            type_is = "Image"
        case "gif": 
            type_is = "Gif"
        case "zip":
            type_is = "Zip File"
        case "pdf":
            type_is = "PDF File"
        case _: 
            type_is = "Could not match"

    return f"{type_is}/{extn}"
            

main()
