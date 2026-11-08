file = input("File name: ")

match file.lower():
    case file if '.gif' in file:
        print(f"image/gif")
    case file if '.jpg' in file or '.jpeg' in file:
        print("image/jpeg")
    case file if '.png' in file:
        print("image/png")
    case file if '.pdf' in file:
        print("application/pdf")
    case file if '.txt' in file:
        print("text/plain")
    case file if '.zip' in file:
        print("application/zip")
    case _:
        print("application/octet-stream")
