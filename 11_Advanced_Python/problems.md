# 11 - Advanced Python Practice Problems

## Beginner Problems

### Problem 1: Simple Iterator
Create a simple iterator that generates numbers from 1 to n.

```python
class NumberIterator:
    # Your code here
    pass

iter_obj = NumberIterator(3)
for num in iter_obj:
    print(num)
```

---

### Problem 2: Simple Generator
Create a generator that yields even numbers up to n.

```python
def even_generator(n):
    # Your code here
    pass

for num in even_generator(10):
    print(num)
```

---

### Problem 3: Basic Decorator
Create a decorator that prints function name before execution.

```python
def print_decorator(func):
    # Your code here
    pass

@print_decorator
def add(a, b):
    return a + b
```

---

## Intermediate Problems

### Problem 4: Decorator with Arguments
Create a decorator that repeats function execution n times.

```python
def repeat(times):
    # Your code here
    pass

@repeat(times=3)
def say_hello():
    print("Hello")
```

---

### Problem 5: Counter with Closure
Create a counter that increments using closure.

```python
def make_counter():
    # Your code here
    pass

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

---

## Advanced Problems

### Problem 6: Stacked Decorators
Apply multiple decorators to a function.

```python
def decorator1(func):
    # Your code here
    pass

def decorator2(func):
    # Your code here
    pass

@decorator1
@decorator2
def add(a, b):
    return a + b
```

---

### Problem 7: Generator Pipeline
Create a pipeline of generators.

```python
def numbers():
    # Your code here
    pass

def squares(nums):
    # Your code here
    pass
```

---

## Solutions

Check the `solutions.py` file for detailed solutions.
