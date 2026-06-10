# 6️⃣ Functions - Complete Guide

Master function creation, parameters, default arguments, *args, **kwargs, lambda, and recursion.

## Table of Contents

1. [Function Basics](#function-basics)
2. [Parameters](#parameters)
3. [Default Arguments](#default-arguments)
4. [Variable Length Arguments](#variable-length-arguments)
5. [Lambda Functions](#lambda-functions)
6. [Recursion](#recursion)

---

## 🟢 Function Basics

### Creating Functions

```python
# Basic function
def greet():
    print("Hello!")

greet()  # Output: Hello!

# Function with return
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8
```

### Docstrings

```python
def calculate_area(radius):
    """Calculate the area of a circle.
    
    Args:
        radius: The radius of the circle
        
    Returns:
        The area of the circle
    """
    import math
    return math.pi * radius ** 2

# Access docstring
print(calculate_area.__doc__)
help(calculate_area)
```

---

## 🟡 Parameters

### Positional Parameters

```python
def introduce(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

introduce("Alice", 25, "NYC")
# Output: Alice is 25 years old and lives in NYC
```

### Keyword Arguments

```python
def introduce(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

# Order doesn't matter with keywords
introduce(city="LA", age=30, name="Bob")
introduce(name="Charlie", age=35, city="SF")
```

### Mixed Arguments

```python
def greet(greeting, name, excitement="!"):
    return f"{greeting} {name}{excitement}"

print(greet("Hello", "Alice"))           # Hello Alice!
print(greet("Hi", "Bob", "!!!"))         # Hi Bob!!!
print(greet("Hey", "Charlie", "."))      # Hey Charlie.
```

---

## 🟡 Default Arguments

### Basic Defaults

```python
def power(x, n=2):
    return x ** n

print(power(3))        # 9 (uses default n=2)
print(power(3, 3))     # 27 (n=3)
print(power(2, 8))     # 256 (n=8)
```

### Multiple Defaults

```python
def create_user(name, age=18, city="Unknown", active=True):
    return {
        "name": name,
        "age": age,
        "city": city,
        "active": active
    }

print(create_user("Alice"))
print(create_user("Bob", 25))
print(create_user("Charlie", 30, "NYC"))
```

---

## 🟡 Variable Length Arguments

### *args (Positional)

```python
def sum_all(*args):
    """Sum any number of arguments"""
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))           # 6
print(sum_all(1, 2, 3, 4, 5))     # 15
print(sum_all(10))                # 10
```

### **kwargs (Keyword)

```python
def print_info(**kwargs):
    """Print key-value pairs"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# Output:
# name: Alice
# age: 25
# city: NYC
```

### Combined *args and **kwargs

```python
def function(a, b, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

function(1, 2, 3, 4, 5, name="Alice", age=25)
# Output:
# a=1, b=2
# args=(3, 4, 5)
# kwargs={'name': 'Alice', 'age': 25}
```

---

## 🟢 Lambda Functions

### Basic Lambda

```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square_lambda = lambda x: x ** 2

print(square(5))            # 25
print(square_lambda(5))     # 25
```

### Lambda with Multiple Arguments

```python
add = lambda x, y: x + y
print(add(5, 3))  # 8

multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))  # 24
```

### Lambda with map()

```python
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]
```

### Lambda with filter()

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]
```

### Lambda with sorted()

```python
students = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 85},
    {"name": "Charlie", "score": 95}
]

sorted_students = sorted(students, key=lambda x: x["score"])
for student in sorted_students:
    print(f"{student['name']}: {student['score']}")
```

---

## 🔴 Recursion

### Basic Recursion

```python
def countdown(n):
    if n == 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
# Output: 5, 4, 3, 2, 1, Done!
```

### Factorial

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

### Fibonacci

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))  # 13
```

### Binary Search

```python
def binary_search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

numbers = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(numbers, 7, 0, len(numbers) - 1))  # 3
```

---

## 📝 Summary

| Concept | Example |
|---------|---------|
| Function | `def function_name():` |
| Parameters | `def func(a, b, c):` |
| Return | `return value` |
| Default args | `def func(a, b=10):` |
| *args | `def func(*args):` |
| **kwargs | `def func(**kwargs):` |
| Lambda | `lambda x: x**2` |
| Recursion | `def func(n): return func(n-1)` |

---

**Next:** [07_Exception_Handling](../07_Exception_Handling/README.md) →
