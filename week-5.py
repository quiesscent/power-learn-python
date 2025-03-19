"""
Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.
Activity 2: Polymorphism Challenge! 🎭

Create a program that includes animals or vehicles with the same action (like move()).
However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
"""


# Base class for Smartphone
class Smartphone:
    def __init__(self, brand, model, year, battery_life):
        self.brand = brand
        self.model = model
        self.year = year
        self.battery_life = battery_life

    def make_call(self, number):
        return f"Calling {number}...📞"

    def send_message(self, number, message):
        return f"Sending message to {number}: {message} 📱"

    def display_info(self):
        return f"{self.brand} {self.model} ({self.year}) - Battery: {self.battery_life} hours"


# Inheriting from Smartphone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, year, battery_life, cpu_speed, ram_size):
        super().__init__(brand, model, year, battery_life)
        self.cpu_speed = cpu_speed
        self.ram_size = ram_size

    def play_game(self, game_name):
        return f"Playing {game_name} with smooth performance! 🎮"

    def display_info(self):
        return super().display_info() + f" - CPU Speed: {self.cpu_speed}GHz, RAM: {self.ram_size}GB"


# Create an object of each class
phone1 = Smartphone("Samsung", "Galaxy S23", 2023, 20)
gaming_phone1 = GamingPhone("Asus", "ROG Phone 6", 2023, 18, 3.0, 16)

# Displaying Information
print(phone1.display_info())  # Base class info
print(gaming_phone1.display_info())  # Inherited class info

# Calling methods
print(phone1.make_call("123456789"))
print(gaming_phone1.play_game("Call of Duty Mobile"))




# Base class for Animal
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Subclasses for specific animals
class Dog(Animal):
    def move(self):
        return "Running on four legs! 🐕"

class Fish(Animal):
    def move(self):
        return "Swimming in the water! 🐟"

class Bird(Animal):
    def move(self):
        return "Flying in the sky! 🦅"


# Test Polymorphism
animals = [Dog(), Fish(), Bird()]

for animal in animals:
    print(animal.move())  # Each animal moves differently
