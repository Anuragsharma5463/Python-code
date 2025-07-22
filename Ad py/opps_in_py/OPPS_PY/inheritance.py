
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size_kwh):
        super().__init__(brand, model)
        self.battery_size_kwh = battery_size_kwh

    def battery_info(self):
        return f"Battery Size: {self.battery_size_kwh} kWh"

# Creating an instance of ElectricCar
my_tesla = ElectricCar("Tesla", "Model S", 99)
print(my_tesla.full_name())
print(my_tesla.battery_info())

# Creating an instance of Car
my_car = Car("Activa", "Colored")
print(my_car.full_name())