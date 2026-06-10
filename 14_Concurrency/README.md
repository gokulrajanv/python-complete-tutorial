# 1️⃣4️⃣ Multithreading & Multiprocessing - Complete Guide

Master threads, processes, concurrency, and async programming.

## Table of Contents

1. [Threads](#threads)
2. [Processes](#processes)
3. [Async Programming](#async-programming)

---

## 🟡 Threads

### Basic Threading

```python
import threading
import time

def task(name):
    for i in range(3):
        print(f"{name}: {i}")
        time.sleep(1)

thread1 = threading.Thread(target=task, args=("Thread1",))
thread2 = threading.Thread(target=task, args=("Thread2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Done!")
```

### Thread Lock

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        temp = counter
        temp += 1
        counter = temp

threads = []
for _ in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Counter: {counter}")
```

---

## 🟡 Processes

### Basic Multiprocessing

```python
import multiprocessing
import time

def task(name):
    for i in range(3):
        print(f"{name}: {i}")
        time.sleep(1)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=task, args=("Process1",))
    p2 = multiprocessing.Process(target=task, args=("Process2",))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("Done!")
```

### Process Pool

```python
import multiprocessing

def square(n):
    return n * n

if __name__ == '__main__':
    with multiprocessing.Pool(4) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
    
    print(results)  # [1, 4, 9, 16, 25]
```

---

## 🔴 Async Programming

### async/await

```python
import asyncio

async def task(name, delay):
    print(f"Starting {name}")
    await asyncio.sleep(delay)
    print(f"Done {name}")
    return f"{name} result"

async def main():
    result1 = await task("Task1", 2)
    result2 = await task("Task2", 1)
    
    print(result1, result2)

asyncio.run(main())
```

### Gather (Run Concurrently)

```python
import asyncio

async def fetch(url, delay):
    await asyncio.sleep(delay)
    return f"Data from {url}"

async def main():
    results = await asyncio.gather(
        fetch("url1", 2),
        fetch("url2", 1),
        fetch("url3", 3)
    )
    
    for result in results:
        print(result)

asyncio.run(main())
```

---

## 📝 Summary

| Concept | Use Case |
|---------|----------|
| Threading | I/O-bound tasks |
| Multiprocessing | CPU-bound tasks |
| Async/await | I/O-bound with concurrency |

---

**Next:** [15_APIs](../15_APIs/README.md) →
