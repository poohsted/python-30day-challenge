# day4_oop.py

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def speak(self):
        return f"{self.name} says {self.sound}"
    
# Creating objects
dog = Animal("Dog", "Woof")
cat = Animal("Cat", "Meow")

# Using methods
print(dog.speak())
print(cat.speak())

# Inheritance example

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof") # Call Animal's __init__
        self.breed = breed
    
    def fetch(self):
        return f"{self.name} is fetching!"
    
# Create a Dog object
my_dog = Dog("Bobo", "Golden Retriever")

print(my_dog.speak()) # Inherited method
print(my_dog.fetch())
print(f"Breed: {my_dog.breed}")
        
