# ===================================
# 14 - Multithreading & Multiprocessing Examples
# ===================================

import threading
import time
from multiprocessing import Process, Pool
import asyncio

print("\n=== THREADING EXAMPLES ===")

# ===== BASIC THREADING =====
print("\n--- Basic Threading ---")

def worker(name):
    for i in range(3):
        print(f"  {name}: {i}")
        time.sleep(0.2)

threads = []
for i in range(2):
    t = threading.Thread(target=worker, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads completed")

# ===== THREAD SAFETY WITH LOCK =====
print("\n--- Thread Safety with Lock ---")

lock = threading.Lock()
counter = 0

def increment():
    global counter
    with lock:
        for _ in range(100000):
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Final counter: {counter}")

# ===== MULTIPROCESSING EXAMPLES =====
print("\n=== MULTIPROCESSING EXAMPLES ===")

def square(n):
    return n ** 2

if __name__ == '__main__':
    # ===== PROCESS POOL =====
    print("\n--- Process Pool ---")
    with Pool(4) as pool:
        numbers = [1, 2, 3, 4, 5]
        results = pool.map(square, numbers)
        print(f"Squares: {results}")

# ===== ASYNC PROGRAMMING =====
print("\n=== ASYNC PROGRAMMING ===")

async def fetch_data(url, delay):
    print(f"  Fetching {url}...")
    await asyncio.sleep(delay)
    print(f"  Done: {url}")
    return f"Data from {url}"

async def main():
    print("\n--- Async Gather ---")
    results = await asyncio.gather(
        fetch_data("URL1", 0.5),
        fetch_data("URL2", 0.3),
        fetch_data("URL3", 0.4)
    )
    print(f"Results: {results}")

if __name__ == '__main__':
    print("\nRunning async tasks...")
    asyncio.run(main())

print("\nDone!")
