# 10 - Modules & Packages Practice Problems

## 🟢 Beginner Problems

### Problem 1: Import and Use Built-in Module
Use the `math` module to calculate the area of a circle with radius 5.

```python
import math

# Your code here
radius = 5
```

**Expected Output:**
```
Area: 78.5
```

---

### Problem 2: datetime Module
Get the current date and time, then print it in a formatted way.

```python
from datetime import datetime

# Your code here
```

**Expected Output:**
```
Current: 2024-01-15 14:30:45
Year: 2024
```

---

### Problem 3: Random Numbers
Generate 5 random numbers between 1 and 100 and print them.

```python
import random

# Your code here
```

---

### Problem 4: Collections Counter
Given a list of words, count how many times each word appears using Counter.

```python
from collections import Counter

words = ['python', 'java', 'python', 'c++', 'python', 'java']

# Your code here
```

**Expected Output:**
```
python: 3
java: 2
c++: 1
```

---

### Problem 5: JSON Operations
Convert a dictionary to JSON and back to dictionary.

```python
import json

data = {"name": "Alice", "age": 25, "city": "NYC"}

# Your code here
```

---

## 🟡 Intermediate Problems

### Problem 6: Create and Import Custom Module
Create a module with functions for basic math operations, then import and use it.

```python
# math_operations.py should have: add, subtract, multiply, divide

# main.py
from math_operations import *

print(add(10, 5))
```

---

### Problem 7: datetime Calculations
Calculate the number of days between today and a given date.

```python
from datetime import datetime

def days_until(target_date_str):
    # Your code here
    pass

# Test
days = days_until("2024-12-31")
print(f"Days until: {days}")
```

---

### Problem 8: os Module Operations
List all Python files in the current directory.

```python
import os

# Your code here
```

---

### Problem 9: Create a Package
Create a package structure with multiple modules and import from it.

```
utils/
├── __init__.py
├── math_utils.py
└── string_utils.py
```

```python
from utils import math_utils, string_utils
```

---

### Problem 10: Exception Handling in Imports
Write code that tries to import a module and handles ImportError.

```python
try:
    # Your code here
except ImportError:
    # Your code here
```

---

## 🔴 Advanced Problems

### Problem 11: Regular Expressions
Use regex to find all email addresses in a string.

```python
import re

text = "Contact: alice@example.com or bob@test.org"

# Your code here
```

---

### Problem 12: Advanced Collections
Use defaultdict to group items by category.

```python
from collections import defaultdict

items = [
    {"name": "apple", "category": "fruit"},
    {"name": "carrot", "category": "vegetable"},
    {"name": "banana", "category": "fruit"}
]

# Your code here
```

---

### Problem 13: Virtual Environment Setup
Document the steps to:
1. Create a virtual environment
2. Activate it
3. Install packages
4. Create requirements.txt

---

### Problem 14: pip Operations
Write code to install, list, and get info about packages programmatically.

---

### Problem 15: Module Aliasing
Create a scenario where you import the same module with different aliases and use them.

```python
import numpy as np
import numpy as numerical_python

# Your code here
```

---

## Solutions

Check the `solutions.py` file for detailed solutions.
