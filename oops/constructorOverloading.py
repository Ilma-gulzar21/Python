class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)


p1 = Person("Ilma")
p2 = Person("Ilma", 22)
p3 = Person("Ilma", 22, "Aligarh")

p1.display()
print()

p2.display()
print()

p3.display()