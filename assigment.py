class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def display_info(self):
        print(f"Smartphone: {self.brand} {self.model}, Price: ${self.price}")
    
    def power_on(self):
        print(f"{self.brand} {self.model} is powering on...")

class GamingPhone(Smartphone):
    def __init__(self, brand, model, price, cooling_system):
        super().__init__(brand, model, price)
        self.cooling_system = cooling_system
    
    def display_info(self):
       
        print(f"Gaming Phone: {self.brand} {self.model} with {self.cooling_system} cooling, Price: ${self.price}")

    def power_on(self):
        print(f"{self.brand} {self.model} is powering on with gaming mode activated!")

class Animal:
    def move(self):
        pass 

class Dog(Animal):
    def move(self):
        print("Dog is running 🐕")

class Bird(Animal):
    def move(self):
        print("Bird is flying 🐦")

class Fish(Animal):
    def move(self):
        print("Fish is swimming 🐟")


print("=== Smartphone Demo ===")
phone = Smartphone("Apple", "iPhone 15", 999)
phone.display_info()
phone.power_on()

print("\n=== GamingPhone Demo (Inheritance and Polymorphism) ===")
g_phone = GamingPhone("Asus", "ROG Phone 7", 1299, "advanced liquid cooling")
g_phone.display_info()
g_phone.power_on()

print("\n=== Polymorphism Demo with Animals ===")
animals = [Dog(), Bird(), Fish()]
for animal in animals:
    animal.move()
