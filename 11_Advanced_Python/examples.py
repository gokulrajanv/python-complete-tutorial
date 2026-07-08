# ===================================
# 11 - Advanced Python Examples
# ===================================

# ===== ITERATORS =====
print("\n=== ITERATORS ===")

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

counter = CountUp(3)
print("Custom iterator:")
for num in counter:
    print(f"  {num}")

# ===== GENERATORS =====
print("\n=== GENERATORS ===")

def countdown(n):
    while n > 0:
        yield n
        n -= 1

print("Generator countdown:")
for num in countdown(3):
    print(f"  {num}")

# ===== DECORATORS =====
print("\n=== DECORATORS ===")

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"  Before: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"  After: returned {result}")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print("Decorated function:")
result = add(5, 3)

# ===== CLOSURES =====
print("\n=== CLOSURES ===")

def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

times3 = multiplier(3)
times5 = multiplier(5)

print(f"times3(10) = {times3(10)}")
print(f"times5(10) = {times5(10)}")

# ===== CONTEXT MANAGERS =====
print("\n=== CONTEXT MANAGERS ===")

class SimpleContext:
    def __enter__(self):
        print("  Entering context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("  Exiting context")
        return False

print("Using context manager:")
with SimpleContext() as ctx:
    print("  Inside context")

print("\nDone!")
