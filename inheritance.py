class Vehicle:
    def move(self):
        return "This vehicle is moving."

class Car(Vehicle):
    def move(self):
        return "Car is driven on the road!"

class Plane(Vehicle):
    def move(self):
        return "Plane flies in the sky!"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedalled along the path!"

# Create different vehicles
vehicles = [Car(), Plane(), Bicycle()]

# Demonstrate polymorphism
for v in vehicles:
    print(v.move())
