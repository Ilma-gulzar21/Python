try:
    with open("unknown.txt", "r") as f:
        data = f.read()
        print(data)

except FileNotFoundError:
    print("File does not exist!")
