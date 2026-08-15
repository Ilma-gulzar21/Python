num = input("Enter a number = ")
num = int(num)
fact = 1

for i in range(1,num+1):
    fact = fact*i

print("factorial = {}".format(fact))
