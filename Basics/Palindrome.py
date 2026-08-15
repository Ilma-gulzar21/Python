def palindrome(num1): 
 num2 = num1
 rev = 0
 while(num1 > 0):
    digit = num1 % 10
    rev = rev*10+digit
    num1 = num1 //10


 if rev == num2:
   print("{} is Palindrome".format(num2))
 else:
   print("{} is not  Palindrome".format(num2))


num = input("Enter a Number = ")
num = int(num)
palindrome(num)