# ===================================
# 10 - Modules & Packages Examples
# ===================================

import os
import sys
import random
import math
from datetime import datetime, timedelta
from collections import Counter
import json

print("\n=== MODULES AND PACKAGES ===")

# ===== OS MODULE =====
print("\n--- OS Module ---")
print(f"Current directory: {os.getcwd()}")
print(f"Python files in current dir: {[f for f in os.listdir('.') if f.endswith('.py')][:3]}")

# ===== SYS MODULE =====
print("\n--- SYS Module ---")
print(f"Python version: {sys.version.split()[0]}")
print(f"Platform: {sys.platform}")
print(f"Python executable: {sys.executable}")

# ===== DATETIME MODULE =====
print("\n--- DateTime Module ---")
now = datetime.now()
print(f"Current date/time: {now}")
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")

future = now + timedelta(days=7)
print(f"7 days later: {future}")

yesterday = now - timedelta(days=1)
print(f"Yesterday: {yesterday}")

# ===== RANDOM MODULE =====
print("\n--- Random Module ---")
print(f"Random float: {random.random():.2f}")
print(f"Random int (1-10): {random.randint(1, 10)}")
print(f"Random choice: {random.choice(['apple', 'banana', 'cherry'])}")

random_list = [1, 2, 3, 4, 5]
random.shuffle(random_list)
print(f"Shuffled list: {random_list}")

# ===== MATH MODULE =====
print("\n--- Math Module ---")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")
print(f"Floor of 4.7: {math.floor(4.7)}")
print(f"Absolute value of -5: {abs(-5)}")
print(f"sin(90°): {math.sin(math.radians(90))}")
print(f"cos(0°): {math.cos(math.radians(0))}")
print(f"Pi: {math.pi}")
print(f"E: {math.e}")

# ===== COLLECTIONS MODULE =====
print("\n--- Collections Module ---")

# Counter
fruits = ['apple', 'banana', 'apple', 'cherry', 'apple', 'banana']
counter = Counter(fruits)
print(f"Fruit count: {counter}")
print(f"Most common: {counter.most_common(1)}")

# ===== JSON MODULE =====
print("\n--- JSON Module ---")
student = {
    "name": "Alice",
    "age": 20,
    "grades": [85, 90, 88],
    "is_active": True
}

json_string = json.dumps(student, indent=2)
print(f"JSON string:\n{json_string}")

parsed = json.loads(json_string)
print(f"Parsed: {parsed['name']}, Age: {parsed['age']}")

# ===== MODULE ATTRIBUTES =====
print("\n--- Module Attributes ---")
import math
print(f"Math module name: {math.__name__}")
print(f"Math dir (first 5): {dir(math)[:5]}")

print("\nDone!")
