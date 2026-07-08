# 14️⃣ Multithreading & Multiprocessing - Complete Guide

Master Threads, Processes, and Async Programming.

## Table of Contents

1. [Multithreading](#multithreading)
2. [Thread Safety](#thread-safety)
3. [Multiprocessing](#multiprocessing)
4. [Async Programming](#async-programming)

---

## 🟢 Multithreading

### Thread Basics

```python
import threading
import time

def worker(name):
    for i in range(3):
        print(f"{name} working - {i}")
        time.sleep(1)

# Create thread
thread = threading.Thread(target=worker, args=("Thread-1",))
thread.start()  # Start thread
thread.join()   # Wait for thread to complete
print("Thread finished")
```

### Multiple Threads

```python
import threading
import time

def worker(name):
    for i in range(2):
        print(f"{name}: {i}")
        time.sleep(0.5)

# Create multiple threads
threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"Worker-{i}",))
    threads.append(t)
    t.start()

# Wait for all threads
for t in threads:
    t.join()

print("All threads finished")
```

---

## 🟡 Thread Safety

### Lock (Mutex)

```python
import threading

lock = threading.Lock()
counter = 0

def increment():
    global counter
    with lock:
        for _ in range(100000):
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Counter: {counter}")  # 500000 (correct)
```

### Semaphore

```python
import threading
import time

semaphore = threading.Semaphore(2)  # Max 2 concurrent

def limited_resource():
    with semaphore:
        print(f"Using resource - {threading.current_thread().name}")
        time.sleep(1)

threads = [threading.Thread(target=limited_resource) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

### Queue

```python
import threading
from queue import Queue

queue = Queue()

def producer():
    for i in range(5):
        queue.put(f"Item {i}")
        print(f"Produced: Item {i}")

def consumer():
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        queue.task_done()

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)

p.start()
c.start()

p.join()
queue.put(None)  # Signal consumer to stop
c.join()
```

---

## 🟡 Multiprocessing

### Process Basics

```python
from multiprocessing import Process
import time

def worker(name):
    for i in range(3):
        print(f"{name}: {i}")
        time.sleep(0.5)

if __name__ == '__main__':
    p = Process(target=worker, args=("Process-1",))
    p.start()
    p.join()
    print("Process finished")
```

### Process Pool

```python
from multiprocessing import Pool

def square(n):
    return n ** 2

if __name__ == '__main__':
    with Pool(4) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
        print(results)  # [1, 4, 9, 16, 25]
```

---

## 🔴 Async Programming

### async/await

```python
import asyncio

async def fetch_data(url):
    print(f"Fetching {url}")
    await asyncio.sleep(2)
    return f"Data from {url}"

async def main():
    result = await fetch_data("https://example.com")
    print(result)

asyncio.run(main())
```

### Multiple Coroutines

```python
import asyncio

async def task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} completed")
    return f"Result {name}"

async def main():
    results = await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3)
    )
    print(results)

asyncio.run(main())
```

---

**Next:** [15_APIs](../15_APIs/README.md) →
