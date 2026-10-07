li1=[]
li2=[]
merge=[]
print("enter element in the first list")
for i in range(5):
    li1.append(input())

print("enter element in the second list")
for i in range(5):
    li2.append(input())
merge=li1+li2
print(sorted(merge))
