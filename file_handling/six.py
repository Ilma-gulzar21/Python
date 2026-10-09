with open("paragraph.txt", "w") as f:
    f.write("Python is easy\n")
    f.write("File handling is useful")

with open("paragraph.txt", "r") as f:
    data = f.read()

lines = data.splitlines()
words = data.split()
characters = len(data)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)
