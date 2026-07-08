# ===================================
# 09 - Object-Oriented Programming Examples
# ===================================

# ===== BASIC CLASS =====
print("\n=== BASIC CLASS ===")

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")
    
    def get_info(self):
        return f"{self.name} is a {self.age} year old {self.breed}"

dog1 = Dog("Buddy", 3, "Golden Retriever")
dog2 = Dog("Max", 5, "German Shepherd")

dog1.bark()  # Buddy says: Woof! Woof!
print(dog1.get_info())  # Buddy is a 3 year old Golden Retriever

# ===== INHERITANCE =====
print("\n=== INHERITANCE ===")

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

class Parrot(Animal):
    def speak(self):
        print(f"{self.name} says: Squawk!")

cat = Cat("Whiskers")
parrot = Parrot("Polly")

cat.speak()      # Whiskers says: Meow!
parrot.speak()   # Polly says: Squawk!

# ===== POLYMORPHISM =====
print("\n=== POLYMORPHISM ===")

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4)]
for shape in shapes:
    print(f"Area: {shape.area():.2f}")

# ===== ENCAPSULATION =====
print("\n=== ENCAPSULATION ===")

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid amount")
    
    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
account.deposit(500)      # Deposited $500. New balance: $1500
account.withdraw(200)     # Withdrawn $200. New balance: $1300
print(f"Balance: ${account.get_balance()}")  # Balance: $1300

# ===== SUPER() FUNCTION =====
print("\n=== SUPER() FUNCTION ===")

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.year = year
    
    def info(self):
        return f"{super().info()} ({self.year})"

car = Car("Toyota", "Camry", 2023)
print(car.info())  # Toyota Camry (2023)

# ===== STATIC METHOD =====
print("\n=== STATIC METHOD ===")

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

print(Calculator.add(5, 3))      # 8
print(Calculator.multiply(5, 3))  # 15

# ===== CLASS METHOD =====
print("\n=== CLASS METHOD ===")

class Person:
    population = 0
    
    def __init__(self, name):
        self.name = name
        Person.population += 1
    
    @classmethod
    def get_population(cls):
        return cls.population

p1 = Person("Alice")
p2 = Person("Bob")
p3 = Person("Charlie")

print(f"Total people: {Person.get_population()}")  # Total people: 3

# ===== PROPERTY DECORATOR =====
print("\n=== PROPERTY DECORATOR ===")

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")     # Celsius: 25°C
print(f"Fahrenheit: {temp.fahrenheit}°F")  # Fahrenheit: 77.0°F
temp.celsius = 0
print(f"Fahrenheit: {temp.fahrenheit}°F")  # Fahrenheit: 32.0°F

# ===== __STR__ AND __REPR__ =====
print("\n=== __STR__ AND __REPR__ ===")

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

book = Book("1984", "George Orwell", 328)
print(book)          # 1984 by George Orwell
print(repr(book))    # Book('1984', 'George Orwell', 328)
