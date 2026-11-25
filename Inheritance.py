class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        return f"{self.brand} engine started"
class Car(Vehicle):
    def drive(self):
        return f"{self.brand} car is driving"
my_car = Car("Toyota")
print(my_car.start())
print(my_car.drive())