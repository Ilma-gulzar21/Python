class Online_Store:
 count=0

 def __init__(self,name, price):
  self.name=name
  self.price=price
  Online_Store.count+=1

 def get_info(self) :
  print(f"price of{self.name} is {self.price}")


 @classmethod
 def shop_count(cls):
   print(f"total objects = {cls.count}")

 @staticmethod
 def avg(price,discount):
  print(f"price Average = {price -(price*discount/100)}")

obj1 = Online_Store("laptop1",10_000)
obj2 = Online_Store("laptop2",70_000)
obj3 = Online_Store("laptop3",40_000)
obj4 = Online_Store("laptop4",70_000)

obj1.get_info()
obj2.get_info()
obj3.get_info()
Online_Store.shop_count()
obj1.avg(10_000,12)
