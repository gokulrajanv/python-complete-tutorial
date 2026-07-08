# 14 - Multithreading & Multiprocessing Practice Problems

## Beginner Problems

### Problem 1: Simple Thread
Create a simple thread that prints numbers 1-3.

```python
import threading

def print_numbers():
    # Your code here
    pass

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
```

---

### Problem 2: Multiple Threads
Create 3 threads that each print their thread number.

```python
import threading

# Your code here
```

---

### Problem 3: Basic Async
Create a simple async function and run it.

```python
import asyncio

async def hello():
    # Your code here
    pass

asyncio.run(hello())
```

---

## Intermediate Problems

### Problem 4: Thread Safety
Use lock to prevent race conditions.

```python
import threading

lock = threading.Lock()
counter = 0

def increment():
    # Your code here
    pass
```

---

### Problem 5: Process Pool
Use multiprocessing Pool.

```python
from multiprocessing import Pool

def square(n):
    return n ** 2

if __name__ == '__main__':
    # Your code here
    pass
```

---

## Advanced Problems

### Problem 6: Producer-Consumer Pattern
Implement producer-consumer with Queue.

```python
import threading
from queue import Queue

# Your code here
```

---

### Problem 7: Async Context Manager
Create async context manager.

```python
import asyncio

class AsyncContextManager:
    # Your code here
    pass

async def main():
    # Your code here
    pass

if __name__ == '__main__':
    asyncio.run(main())
```

---

## Solutions

Check the `solutions.py` file for detailed solutions.
