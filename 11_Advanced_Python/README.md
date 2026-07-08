# 11️⃣ Advanced Python - Complete Guide

Master Iterators, Generators, Decorators, Closures, Context Managers, and Garbage Collection.

## Table of Contents

1. [Iterators](#iterators)
2. [Generators](#generators)
3. [Decorators](#decorators)
4. [Closures](#closures)
5. [Context Managers](#context-managers)
6. [Garbage Collection](#garbage-collection)

---

## 🟢 Iterators

### What is an Iterator?

An iterator is an object that implements `__iter__()` and `__next__()` methods.

```python
# Create custom iterator
class CountUp:
    def __init__(self, max):
        self.current = 0
        self.max = max
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# Use iterator
counter = CountUp(3)
for num in counter:
    print(num)  # 1, 2, 3
```

### iter() and next()

```python
mylist = [1, 2, 3]
my_iter = iter(mylist)  # Create iterator

print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
```

---

## 🟡 Generators

### Generator Functions

```python
# Generator uses yield
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Use generator
for num in countdown(3):
    print(num)  # 3, 2, 1
```

### Generator vs Iterator

```python
# Generator - memory efficient
def gen_squares(n):
    for i in range(n):
        yield i ** 2

# Generator is lazy - generates on demand
gen = gen_squares(5)
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4
```

---

## 🟡 Decorators

### Basic Decorator

```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

### Decorator with Arguments

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8
```

---

## 🟡 Closures

### What is a Closure?

A closure is a function with access to the enclosing scope's variables.

```python
def outer(x):
    def inner():
        print(f"x is {x}")
    return inner

func = outer(5)
func()  # x is 5
```

### Closure Example

```python
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

times3 = multiplier(3)
times5 = multiplier(5)

print(times3(10))  # 30
print(times5(10))  # 50
```

---

## 🔴 Context Managers

### with Statement

```python
# Using with statement
with open("file.txt", "r") as file:
    content = file.read()
# File automatically closed
```

### Custom Context Manager

```python
class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        return False

with MyContextManager() as mcm:
    print("Inside context")
```

---

## 🔴 Garbage Collection

### Reference Counting

```python
import sys

x = []  # Reference count = 1
y = x   # Reference count = 2

print(sys.getrefcount(x))  # 3

del y   # Reference count = 2
print(sys.getrefcount(x))  # 2
```

---

**Next:** [12_DSA](../12_DSA/README.md) →
