# 09 - Object-Oriented Programming Practice Problems

## 🟢 Beginner Problems

### Problem 1: Simple Class
Create a `Student` class with attributes: name, age, and grade. Add a method to display student information.

```python
class Student:
    # Your code here
    pass

student = Student("Alice", 20, "A")
student.display_info()
```

**Expected Output:**
```
Name: Alice
Age: 20
Grade: A
```

---

### Problem 2: Class with Methods
Create a `Rectangle` class with methods to calculate area and perimeter.

```python
class Rectangle:
    # Your code here
    pass

rect = Rectangle(5, 10)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
```

**Expected Output:**
```
Area: 50
Perimeter: 30
```

---

### Problem 3: Basic Inheritance
Create an `Animal` class and a `Dog` class that inherits from it.

```python
class Animal:
    # Your code here
    pass

class Dog(Animal):
    # Your code here
    pass

dog = Dog("Buddy")
dog.speak()  # Buddy barks
```

---

### Problem 4: Class Attributes
Create a `BankAccount` class with balance tracking and methods to deposit and withdraw.

```python
class BankAccount:
    # Your code here
    pass

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())
```

**Expected Output:**
```
1300
```

---

### Problem 5: __str__ Method
Create a `Car` class and implement the `__str__` method for proper representation.

```python
class Car:
    # Your code here
    pass

car = Car("Toyota", "Camry", 2023)
print(car)
```

**Expected Output:**
```
2023 Toyota Camry
```

---

## 🟡 Intermediate Problems

### Problem 6: Multi-level Inheritance
Create a hierarchy: Vehicle -> Car -> ElectricCar with appropriate attributes and methods.

```python
class Vehicle:
    # Your code here
    pass

class Car(Vehicle):
    # Your code here
    pass

class ElectricCar(Car):
    # Your code here
    pass

car = ElectricCar("Tesla", "Model 3", 2023, "75 kWh")
car.info()
```

---

### Problem 7: Polymorphism
Create different shape classes with an area() method. Store them in a list and calculate total area.

```python
class Circle:
    # Your code here
    pass

class Rectangle:
    # Your code here
    pass

shapes = [Circle(5), Rectangle(4, 6)]
total_area = sum(shape.area() for shape in shapes)
print(f"Total area: {total_area}")
```

---

### Problem 8: Encapsulation
Create a `Password` class with private attributes and validation.

```python
class Password:
    def __init__(self, pwd):
        self.__password = pwd
    
    def is_strong(self):
        # Check if password is strong (at least 8 chars, has letters and numbers)
        pass
    
    def change_password(self, new_pwd):
        # Your code here
        pass

pwd = Password("MyPassword123")
print(pwd.is_strong())  # True
```

---

### Problem 9: Super() Function
Use super() to call parent class methods in a child class.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        # Use super() here
        pass
    
    def display(self):
        # Call parent display() and add student_id
        pass

student = Student("Alice", 20, "S123")
student.display()
```

**Expected Output:**
```
Name: Alice, Age: 20
Student ID: S123
```

---

### Problem 10: Static Methods
Create a `MathOperations` class with static methods for common operations.

```python
class MathOperations:
    @staticmethod
    def add(a, b):
        # Your code here
        pass
    
    @staticmethod
    def multiply(a, b):
        # Your code here
        pass

print(MathOperations.add(5, 3))      # 8
print(MathOperations.multiply(5, 3))  # 15
```

---

### Problem 11: Class Methods
Create a class with a counter using class methods.

```python
class Book:
    book_count = 0
    
    def __init__(self, title):
        self.title = title
        Book.book_count += 1
    
    @classmethod
    def get_book_count(cls):
        # Your code here
        pass

b1 = Book("Python 101")
b2 = Book("Data Science")
print(Book.get_book_count())  # 2
```

---

### Problem 12: Properties
Create a class with properties to validate input.

```python
class Age:
    def __init__(self, age):
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0 or value > 150:
            raise ValueError("Invalid age")
        self._age = value

person_age = Age(25)
print(person_age.age)  # 25
person_age.age = 30
print(person_age.age)  # 30
```

---

## 🔴 Advanced Problems

### Problem 13: Abstract Base Class
Create an abstract class for Shapes with abstract methods.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Your code here
```

---

### Problem 14: Multiple Inheritance
Create a class that inherits from multiple parent classes.

```python
class Flyer:
    def fly(self):
        print("Flying...")

class Swimmer:
    def swim(self):
        print("Swimming...")

class Duck(Flyer, Swimmer):
    pass

duck = Duck()
duck.fly()    # Flying...
duck.swim()   # Swimming...
```

---

### Problem 15: Complex Object Relationships
Create a `Library` class that manages multiple `Book` objects.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        # Your code here
        pass
    
    def find_books_by_author(self, author):
        # Your code here
        pass
    
    def list_all_books(self):
        # Your code here
        pass

library = Library("City Library")
# Add books and test methods
```

---

### Problem 16: Mixin Classes
Create mixin classes to add functionality to other classes.

```python
class TimestampMixin:
    def get_timestamp(self):
        from datetime import datetime
        return datetime.now()

class LogMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class Document(TimestampMixin, LogMixin):
    def __init__(self, title):
        self.title = title

doc = Document("My Doc")
doc.log("Document created")
print(doc.get_timestamp())
```

---

### Problem 17: Context Manager
Create a context manager using `__enter__` and `__exit__`.

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        # Your code here
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Your code here
        pass

# Usage:
# with FileManager("test.txt", "w") as f:
#     f.write("Hello")
```

---

### Problem 18: Observer Pattern
Implement a simple observer pattern.

```python
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        # Your code here
        pass
    
    def notify(self, data):
        for observer in self._observers:
            observer.update(data)

class Observer:
    def update(self, data):
        print(f"Observer received: {data}")

# Test the pattern
```

---

### Problem 19: Factory Pattern
Implement a factory pattern to create objects.

```python
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args):
        if shape_type == "circle":
            return Circle(args[0])
        elif shape_type == "rectangle":
            return Rectangle(args[0], args[1])
        else:
            raise ValueError("Unknown shape")

# Usage
shape = ShapeFactory.create_shape("circle", 5)
print(shape.area())
```

---

### Problem 20: Singleton Pattern
Implement a singleton class.

```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Test
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

---

## Solutions

Check the `solutions.py` file for detailed solutions to all problems.
