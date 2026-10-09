# Creating a file
with open("students.txt", "w") as f:
    f.write("Aman\n")
    f.write("Sara\n")
    f.write("Rahul\n")

# Reading one line
with open("students.txt", "r") as f:
    data = f.readline()
    print(data)

# Reading all lines as a list
with open("students.txt", "r") as f:
    data = f.readlines()
    print(data)

# Reading using a for loop
with open("students.txt", "r") as f:
    for line in f:
        print(line.strip())

# Appending new data
with open("students.txt", "a") as f:
    f.write("Ilma\n")

# Displaying updated file
with open("students.txt", "r") as f:
    print(f.read())
