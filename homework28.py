class Car:
    def fuel_type(self):
        pass
    def max_speed(self):
        pass

class BMW(Car):
    def fuel_type(self):
        return "Petrol"
    def max_speed(self):
        return "250 km/h"

class Ferrari(Car):
    def fuel_type(self):
        return "Petrol (High Octane)"
    def max_speed(self):
        return "350 km/h"

cars = [BMW(), Ferrari()]

for car in cars:
    print(f"{car.__class__.__name__}:")
    print(" Fuel Type:", car.fuel_type())
    print(" Max Speed:", car.max_speed())
    print()
