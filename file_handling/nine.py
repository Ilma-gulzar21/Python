# Creating source file
with open("source.txt", "w") as f:
    f.write("Python File Handling\n")
    f.write("Learning read and write operations")

# Copying content to another file
with open("source.txt", "r") as f:
    data = f.read()

with open("destination.txt", "w") as f:
    f.write(data)

# Reading copied content
with open("destination.txt", "r") as f:
    print(f.read())
