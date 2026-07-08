# 11. Advanced Python

## Overview
Advanced Python concepts help you write more efficient, elegant, and Pythonic code. This section covers iterators, generators, decorators, closures, and more.

## Table of Contents
1. [Iterators & Generators](#iterators--generators)
2. [Decorators](#decorators)
3. [Closures](#closures)
4. [Context Managers](#context-managers)
5. [Virtual Environment](#virtual-environment)
6. [Garbage Collection](#garbage-collection)

---

## Iterators & Generators

### Iterators
An iterator is an object that implements two methods: `__iter__()` and `__next__()`.

```python
# Creating a simple iterator
class CountUp:
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# Using the iterator
counter = CountUp(3)
for num in counter:
    print(num)  # Output: 1, 2, 3

# Using next() directly
counter = CountUp(3)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
# print(next(counter))  # Raises StopIteration
```

### Generators
A generator is a simpler way to create iterators using a function with `yield`.

```python
# Simple generator
def count_up(max):
    current = 0
    while current < max:
        current += 1
        yield current

# Using generator
for num in count_up(3):
    print(num)  # Output: 1, 2, 3

# Generator expression
squares = (x**2 for x in range(5))
print(next(squares))  # 0
print(next(squares))  # 1
print(next(squares))  # 4

# Generator with multiple yields
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for fib in fibonacci(6):
    print(fib)  # Output: 0, 1, 1, 2, 3, 5
```

### Generator Methods
```python
def echo():
    value = None
    while True:
        value = (yield value)

# Using send()
gen = echo()
next(gen)  # Prime the generator
print(gen.send(10))  # 10
print(gen.send(20))  # 20

# Using throw()
def gen_with_exception():
    try:
        yield 1
        yield 2
    except ValueError:
        yield "Exception caught"
    yield 3

gen = gen_with_exception()
print(next(gen))  # 1
print(gen.throw(ValueError))  # Exception caught
```

---

## Decorators

### Function Decorators
A decorator is a function that modifies another function or class.

```python
# Simple decorator
def my_decorator(func):
    def wrapper():
        print("Something before function")
        func()
        print("Something after function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something before function
# Hello!
# Something after function
```

### Decorators with Arguments
```python
# Decorator that takes arguments
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

result = add(5, 3)  # Prints: Calling add
print(result)  # 8
```

### Parameterized Decorators
```python
# Decorator factory
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

### Practical Decorators
```python
import time

# Timer decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

slow_function()

# Type checking decorator
def type_check(**types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, arg_type in types.items():
                if arg in kwargs and not isinstance(kwargs[arg], arg_type):
                    raise TypeError(f"{arg} must be {arg_type}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check(name=str, age=int)
def register(name, age):
    print(f"Registered: {name}, Age: {age}")

register(name="John", age=25)  # Works
# register(name="John", age="25")  # Raises TypeError
```

---

## Closures

### Understanding Closures
A closure is a function that captures variables from its enclosing scope.

```python
# Simple closure
def outer(x):
    def inner(y):
        return x + y
    return inner

add_5 = outer(5)
print(add_5(3))  # 8
print(add_5(7))  # 12

# Closures remember their environment
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

times3 = multiplier(3)
times5 = multiplier(5)

print(times3(10))  # 30
print(times5(10))  # 50
```

### Practical Closures
```python
# Function factory
def make_logger(prefix):
    def log(message):
        print(f"{prefix}: {message}")
    return log

error_log = make_logger("ERROR")
info_log = make_logger("INFO")

error_log("System error")  # ERROR: System error
info_log("System started")  # INFO: System started

# Counter with closure
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    def reset():
        nonlocal count
        count = 0
    return increment, reset

inc, reset = make_counter()
print(inc())    # 1
print(inc())    # 2
print(inc())    # 3
reset()
print(inc())    # 1
```

---

## Context Managers

### Using Context Managers
Context managers handle setup and cleanup operations using `with` statement.

```python
# File handling (built-in context manager)
with open('file.txt', 'r') as f:
    content = f.read()
# File is automatically closed

# Multiple context managers
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    data = infile.read()
    outfile.write(data.upper())
```

### Creating Context Managers
```python
# Using __enter__ and __exit__
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()
        return False

# Using custom context manager
with FileManager('test.txt', 'w') as f:
    f.write("Hello, World!")

# Using contextlib
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Setup")
    try:
        yield
    finally:
        print("Cleanup")

with my_context():
    print("Inside context")
```

---

## Virtual Environment
See section [10. Modules & Packages](../10_Modules_and_Packages/README.md#pip--virtual-environment)

---

## Garbage Collection

### Understanding Garbage Collection
Python automatically manages memory through reference counting and garbage collection.

```python
import gc

# Get garbage collection stats
print(gc.get_count())  # Objects in each generation

# Manual garbage collection
gc.collect()

# Disable automatic collection
gc.disable()
gc.collect()
gc.enable()

# Check if object is tracked
x = [1, 2, 3]
print(gc.is_tracked(x))  # True
print(gc.is_tracked(5))  # False

# Get objects in a generation
gen0_objects = gc.get_objects()
print(len(gen0_objects))
```

### Reference Counting
```python
import sys

# Check reference count
x = []
print(sys.getrefcount(x))  # At least 2 (x and function argument)

y = x
print(sys.getrefcount(x))  # Increased by 1

del y
print(sys.getrefcount(x))  # Decreased by 1
```

### Circular References
```python
import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create circular reference
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1  # Circular reference

# Delete references
del node1
del node2

# Garbage collection cleans up circular references
gc.collect()
```

---

## Practice Exercises

### Exercise 1: Custom Iterator
Create a custom iterator class `RangeIterator` that behaves like the built-in `range()`.

### Exercise 2: Generator Function
Write a generator function that yields Fibonacci numbers up to a given limit.

### Exercise 3: Function Decorator
Create a decorator that logs function calls with arguments and return values.

### Exercise 4: Context Manager
Create a custom context manager for database connections with connection and cleanup.

---

## Key Takeaways
✅ Generators are memory-efficient iterators  
✅ Decorators modify function behavior  
✅ Closures capture variables from outer scope  
✅ Context managers ensure proper resource cleanup  
✅ Understanding garbage collection helps with memory management  

---

## Next Steps
→ Learn about [Data Structures & Algorithms](../12_Data_Structures_and_Algorithms/README.md)
