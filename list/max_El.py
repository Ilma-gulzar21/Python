marks = [28,89,53,93,30,52,12]
max=0

#using index value
n = range(len(marks))
for i in n:
    if max<marks[i]:
         max=marks[i]
print("maximum Element = {}".format(max))



#using direct value
max1=0
for i in marks:
    if max1<i:
         max1=i

print("maximum Element = {}".format(max1))