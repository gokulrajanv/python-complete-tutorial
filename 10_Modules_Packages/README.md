# 1️⃣0️⃣ Modules & Packages - Complete Guide

Master importing, creating modules, packages, pip, and virtual environments.

## Table of Contents

1. [Modules](#modules)
2. [Packages](#packages)
3. [Import Methods](#import-methods)
4. [Built-in Modules](#built-in-modules)
5. [pip & Virtual Environment](#pip--virtual-environment)

---

## 🟢 Modules

### What is a Module?

A module is a Python file containing functions, classes, and variables.

```python
# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

PI = 3.14159
```

### Importing a Module

```python
# main.py
import math_utils

result = math_utils.add(5, 3)
print(result)  # 8
print(math_utils.PI)  # 3.14159
```

### From Import

```python
from math_utils import add, subtract

print(add(10, 5))       # 15
print(subtract(10, 5))  # 5
```

### Import All

```python
from math_utils import *

print(add(5, 3))  # 8
```

### Alias (As)

```python
import math_utils as mu
from math_utils import add as addition

print(mu.add(5, 3))  # 8
print(addition(5, 3))  # 8
```

### __name__ Variable

```python
# my_module.py
def greet():
    print("Hello!")

if __name__ == "__main__":
    greet()  # Runs only when executed directly
```

### Module Attributes

```python
import math_utils

print(dir(math_utils))  # List all attributes
print(math_utils.__name__)  # Module name
print(math_utils.__file__)  # File path
doc(math_utils.add)  # Function documentation
```

---

## 🟡 Packages

### What is a Package?

A package is a directory containing an `__init__.py` file and modules.

### Package Structure

```
my_package/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

### __init__.py

```python
# my_package/__init__.py
print("Package initialized")

# Make functions available at package level
from .module1 import my_function

__all__ = ['my_function', 'another_function']
```

### Importing from Package

```python
# Import module from package
from my_package import module1
from my_package.module1 import my_function

# Import from subpackage
from my_package.subpackage import module3
```

### Package with Subpackages

```
utils/
├── __init__.py
├── math_ops/
│   ├── __init__.py
│   ├── basic.py
│   └── advanced.py
└── string_ops/
    ├── __init__.py
    └── formatting.py
```

```python
from utils.math_ops.basic import add
from utils.string_ops.formatting import uppercase
```

---

## 🟡 Import Methods

### Absolute Import

```python
# From root directory
from my_package.module1 import my_function
from my_package.subpackage.module3 import another_function
```

### Relative Import

```python
# my_package/module1.py
from . import module2  # Same directory
from .subpackage import module3  # Subdirectory
from .. import other_package  # Parent directory
```

### Conditional Import

```python
try:
    import numpy as np
except ImportError:
    print("NumPy not installed")
    np = None

if np:
    array = np.array([1, 2, 3])
```

### Dynamic Import

```python
import importlib

module_name = "math_utils"
module = importlib.import_module(module_name)
result = module.add(5, 3)
```

---

## 🟡 Built-in Modules

### os - Operating System

```python
import os

print(os.getcwd())  # Current directory
os.chdir("..")  # Change directory
files = os.listdir(".")  # List files
print(os.path.exists("file.txt"))  # Check if exists
```

### sys - System

```python
import sys

print(sys.version)  # Python version
print(sys.platform)  # Platform
print(sys.path)  # Module search paths
sys.exit()  # Exit program
```

### datetime - Date and Time

```python
from datetime import datetime, timedelta

now = datetime.now()
print(now)  # Current date and time

future = now + timedelta(days=7)
print(future)  # 7 days later
```

### random - Random Numbers

```python
import random

print(random.random())  # Float 0-1
print(random.randint(1, 10))  # Integer 1-10
print(random.choice([1, 2, 3]))  # Random choice
print(random.shuffle([1, 2, 3]))  # Shuffle list
```

### math - Mathematical Functions

```python
import math

print(math.sqrt(16))  # 4
print(math.ceil(4.3))  # 5
print(math.floor(4.7))  # 4
print(math.pi)  # 3.14159
print(math.sin(math.pi/2))  # 1
```

### collections - Data Structures

```python
from collections import Counter, defaultdict, namedtuple

# Counter
frequency = Counter([1, 1, 2, 2, 2, 3])
print(frequency)  # Counter({2: 3, 1: 2, 3: 1})

# defaultdict
dd = defaultdict(list)
dd["key"].append("value")

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
```

### json - JSON

```python
import json

data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)  # Dict to JSON string
parsed = json.loads(json_string)  # JSON string to dict
```

### re - Regular Expressions

```python
import re

text = "Hello 123 World 456"
pattern = r"\d+"
matches = re.findall(pattern, text)
print(matches)  # ['123', '456']
```

---

## 🔴 pip & Virtual Environment

### pip - Package Manager

```bash
# Install package
pip install requests

# Install specific version
pip install requests==2.28.0

# Install multiple packages
pip install requests django numpy

# List installed packages
pip list

# Show package info
pip show requests

# Upgrade package
pip install --upgrade requests

# Uninstall package
pip uninstall requests

# Save dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

### Virtual Environment

```bash
# Create virtual environment
python -m venv env

# Activate (Windows)
env\Scripts\activate

# Activate (Mac/Linux)
source env/bin/activate

# Deactivate
deactivate

# Inside virtual environment, pip installs only there
pip install requests

# Create requirements file
pip freeze > requirements.txt
```

### requirements.txt Example

```
requests==2.28.0
django==4.1.0
numpy==1.23.0
pandas>=1.4.0
flask
```

---

## 📝 Summary

| Concept | Description | Example |
|---------|-------------|----------|
| Module | Python file with functions/classes | `import module_name` |
| Package | Directory with modules | `from package import module` |
| Import | Load module/function | `import numpy as np` |
| pip | Package manager | `pip install requests` |
| venv | Virtual environment | `python -m venv env` |
| requirements.txt | Dependencies file | `pip freeze > requirements.txt` |

---

**Next:** [11_Advanced_Python](../11_Advanced_Python/README.md) →
