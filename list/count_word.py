f = open("text.txt","r")
for line in f:
    data=line.split()
    print(len(data))
