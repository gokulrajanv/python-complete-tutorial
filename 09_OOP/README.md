# 9️⃣ Object-Oriented Programming (OOP) - Complete Guide

Master Classes, Objects, Inheritance, Polymorphism, Encapsulation, and Abstraction.

## Table of Contents

1. [Classes & Objects](#classes--objects)
2. [Constructors & Attributes](#constructors--attributes)
3. [Methods](#methods)
4. [Inheritance](#inheritance)
5. [Polymorphism](#polymorphism)
6. [Encapsulation](#encapsulation)
7. [Static & Class Methods](#static--class-methods)

---

## 🟢 Classes & Objects

### Creating a Class

```python
class Dog:
    """A simple Dog class"""
    pass

# Create an object (instance)
dog1 = Dog()
print(type(dog1))  # <class '__main__.Dog'>
```

### Class with Attributes

```python
class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

# Create instances
dog1 = Dog("Buddy", 3, "Golden Retriever")
dog2 = Dog("Max", 5, "German Shepherd")

print(dog1.name)  # Buddy
print(dog2.breed)  # German Shepherd
```

---

## 🟢 Constructors & Attributes

### __init__ Method

```python
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

person1 = Person("Alice", 25, "alice@example.com")
print(f"Name: {person1.name}")
print(f"Email: {person1.email}")
```

### Class Attributes vs Instance Attributes

```python
class Car:
    wheels = 4  # Class attribute (shared by all instances)
    
    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute
        self.model = model

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(Car.wheels)  # 4
print(car1.wheels)  # 4
print(car1.brand)   # Toyota
print(car2.brand)   # Honda
```

### __str__ and __repr__ Methods

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 25)
print(str(person))   # Alice is 25 years old
print(repr(person))  # Person('Alice', 25)
print(person)        # Alice is 25 years old
```

---

## 🟡 Methods

### Instance Methods

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says Woof!")
    
    def get_age(self):
        return self.age
    
    def celebrate_birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old")

dog = Dog("Buddy", 3)
dog.bark()  # Buddy says Woof!
print(dog.get_age())  # 3
dog.celebrate_birthday()  # Buddy is now 4 years old
```

### Method with Parameters

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def resize(self, length, width):
        self.length = length
        self.width = width
        print(f"Resized to {length}x{width}")

rect = Rectangle(5, 10)
print(f"Area: {rect.area()}")  # Area: 50
print(f"Perimeter: {rect.perimeter()}")  # Perimeter: 30
rect.resize(7, 12)  # Resized to 7x12
```

---

## 🟡 Inheritance

### Basic Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()  # Buddy barks
cat.speak()  # Whiskers meows
```

### super() Function

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
    
    def display_info(self):
        super().display_info()  # Call parent method
        print(f"Student ID: {self.student_id}")

student = Student("Alice", 20, "S123")
student.display_info()
# Output:
# Name: Alice, Age: 20
# Student ID: S123
```

### Multi-level Inheritance

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def info(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

car = ElectricCar("Tesla", "Model 3", "75 kWh")
car.info()  # Brand: Tesla
print(f"Model: {car.model}")
print(f"Battery: {car.battery}")
```

---

## 🟡 Polymorphism

### Method Overriding

```python
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(animal.make_sound())
# Output:
# Woof!
# Meow!
# Moo!
```

### Duck Typing

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Person:
    def speak(self):
        return "Hello!"

def make_it_speak(entity):
    print(entity.speak())

make_it_speak(Dog())    # Woof!
make_it_speak(Cat())    # Meow!
make_it_speak(Person()) # Hello!
```

---

## 🟡 Encapsulation

### Public, Protected, and Private Attributes

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Public
        self._account_number = "1234567890"  # Protected (convention)
        self.__balance = balance  # Private
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ${amount}")
        else:
            print("Invalid amount")
    
    def get_balance(self):
        return self.__balance
    
    def __format_balance(self):  # Private method
        return f"${self.__balance:.2f}"

account = BankAccount("Alice", 1000)
account.deposit(500)  # Deposited $500
account.withdraw(200)  # Withdrawn $200
print(account.get_balance())  # 1300
print(account.owner)  # Alice
# print(account.__balance)  # ERROR - private attribute
```

### Properties and Setters

```python
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
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0
temp.fahrenheit = 86
print(temp.celsius)     # 30.0
```

---

## 🟡 Static & Class Methods

### Static Methods

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

print(Math.add(5, 3))        # 8
print(Math.multiply(5, 3))   # 15

math_obj = Math()
print(math_obj.add(10, 5))   # 15
```

### Class Methods

```python
class Counter:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Counter.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @classmethod
    def reset_count(cls):
        cls.count = 0

c1 = Counter("First")
c2 = Counter("Second")
c3 = Counter("Third")

print(Counter.get_count())  # 3
Counter.reset_count()
print(Counter.get_count())  # 0
```

---

## 🔴 Abstraction

### Abstract Base Classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

circle = Circle(5)
rect = Rectangle(4, 6)

print(f"Circle area: {circle.area()}")  # Circle area: 78.5
print(f"Rectangle area: {rect.area()}")  # Rectangle area: 24

# shape = Shape()  # ERROR - cannot instantiate abstract class
```

---

## 📝 OOP Principles Summary

| Principle | Description | Example |
|-----------|-------------|----------|
| **Encapsulation** | Bundle data and methods; hide internal details | Private attributes with getters/setters |
| **Inheritance** | Derive new classes from existing ones | `class Dog(Animal)` |
| **Polymorphism** | Objects can take multiple forms | Method overriding |
| **Abstraction** | Hide complexity; expose only essentials | Abstract classes and methods |

---

**Next:** [10_Modules_Packages](../10_Modules_Packages/README.md) →
