marks = [28,89,53,93,30,52,12]
max=0
n = range(len(marks))
for i in n:
    if max<marks[i]:
         max=marks[i]

print("maximum Element = {}".format(max))