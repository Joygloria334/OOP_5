# Base class: Instrument
class Instrument:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def play(self):
        return f"{self.name} is making music!"

# Derived class: Guitar
class Guitar(Instrument):
    def __init__(self, name, brand, strings):
        super().__init__(name, brand)
        self.strings = strings

    def play(self):  # Polymorphism (method overriding)
        return f"{self.brand} {self.name} strums with {self.strings} strings!"

# Derived class: Piano
class Piano(Instrument):
    def __init__(self, name, brand, keys):
        super().__init__(name, brand)
        self.keys = keys

    def play(self):
        return f"{self.brand} {self.name} plays with {self.keys} keys!"

# Create unique objects
guitar = Guitar("Acoustic", "Yamaha", 6)
piano = Piano("Grand Piano", "Steinway", 88)

print(guitar.play())
print(piano.play())
