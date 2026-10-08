class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Seats:", self.seats)


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Engine CC:", self.engine_cc)


car = Car("Toyota", "Fortuner", 7)
bike = Bike("Honda", "Shine", 125)

car.display()
print()
bike.display()