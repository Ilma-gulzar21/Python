# Writing data into a file
f = open("data.txt", "w")
f.write("Hello Python\n")
f.write("Learning File Handling")
f.close()

# Reading data from a file
f = open("data.txt", "r")
data = f.read()
print(data)
f.close()
