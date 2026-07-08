# 10. Modules & Packages

## Overview
Modules and packages are fundamental to organizing and reusing Python code. This section covers how to create, import, and manage modules and packages effectively.

## Table of Contents
1. [Import Modules](#import-modules)
2. [Create Modules & Packages](#create-modules--packages)
3. [pip & Virtual Environment](#pip--virtual-environment)

---

## Import Modules

### Built-in Modules
Python comes with many built-in modules you can use without installing anything.

```python
# Importing entire module
import math
print(math.sqrt(16))  # Output: 4.0
print(math.pi)        # Output: 3.14159...

# Importing specific functions
from math import sqrt, pi
print(sqrt(16))       # Output: 4.0
print(pi)             # Output: 3.14159...

# Importing with aliases
import math as m
print(m.sqrt(25))     # Output: 5.0

from math import sqrt as square_root
print(square_root(36))  # Output: 6.0
```

### Common Built-in Modules

#### os Module
```python
import os

# Get current working directory
print(os.getcwd())

# List files in directory
print(os.listdir('.'))

# Create directory
os.makedirs('new_folder', exist_ok=True)

# Check if path exists
if os.path.exists('new_folder'):
    print("Directory exists!")

# Remove directory
os.rmdir('new_folder')

# Get environment variables
print(os.getenv('PATH'))
```

#### sys Module
```python
import sys

# Python version
print(sys.version)

# Python path (directories searched for modules)
print(sys.path)

# Add custom path
sys.path.append('/custom/path')

# Command line arguments
print(sys.argv)

# Exit the program
# sys.exit(0)
```

#### datetime Module
```python
from datetime import datetime, timedelta, date

# Current date and time
now = datetime.now()
print(now)

# Current date
today = date.today()
print(today)

# Create specific date
christmas = date(2024, 12, 25)
print(christmas)

# Time difference
delta = timedelta(days=5, hours=3, minutes=30)
future_date = today + delta
print(future_date)

# Format date
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%A, %B %d, %Y"))
```

#### json Module
```python
import json

# Dictionary to JSON string
data = {
    "name": "John",
    "age": 30,
    "courses": ["Python", "JavaScript"]
}

json_string = json.dumps(data, indent=2)
print(json_string)

# JSON string to dictionary
parsed_data = json.loads(json_string)
print(parsed_data)

# Write to JSON file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

# Read from JSON file
with open('data.json', 'r') as f:
    loaded_data = json.load(f)
    print(loaded_data)
```

#### random Module
```python
import random

# Random float between 0 and 1
print(random.random())

# Random integer in range
print(random.randint(1, 10))

# Random choice from list
colors = ['red', 'blue', 'green', 'yellow']
print(random.choice(colors))

# Shuffle list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

# Sample without replacement
print(random.sample(colors, 2))
```

---

## Create Modules & Packages

### Creating a Module
A module is a single `.py` file.

**math_operations.py**
```python
"""
Module for mathematical operations
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

PI = 3.14159
```

### Using the Module
```python
# Import entire module
import math_operations
print(math_operations.add(5, 3))

# Import specific items
from math_operations import add, subtract, PI
print(add(10, 5))
print(subtract(10, 5))
print(PI)
```

### Creating a Package
A package is a directory with an `__init__.py` file.

```
my_package/
    __init__.py
    module1.py
    module2.py
    sub_package/
        __init__.py
        module3.py
```

**my_package/__init__.py**
```python
"""
My Package - A collection of useful modules
"""

from .module1 import function1
from .module2 import function2

__all__ = ['function1', 'function2']
__version__ = '1.0.0'
```

**my_package/module1.py**
```python
def function1():
    return "This is function 1"

def helper():
    return "Helper function"
```

**my_package/module2.py**
```python
def function2():
    return "This is function 2"

class MyClass:
    def method(self):
        return "Class method"
```

**my_package/sub_package/__init__.py**
```python
from .module3 import sub_function
```

**my_package/sub_package/module3.py**
```python
def sub_function():
    return "Sub-package function"
```

### Using the Package
```python
# Import from package
from my_package import function1, function2
print(function1())
print(function2())

# Import subpackage
from my_package.sub_package import sub_function
print(sub_function())

# Access version
import my_package
print(my_package.__version__)

# Check __all__
print(my_package.__all__)
```

### Module Documentation
```python
"""
This is the module docstring.
It describes what the module does.
"""

__version__ = '1.0.0'
__author__ = 'Your Name'
__all__ = ['public_function', 'PublicClass']

def public_function():
    """This function is part of public API"""
    pass

def _private_function():
    """This function is private (starts with _)"""
    pass

class PublicClass:
    """This class is part of public API"""
    pass
```

---

## pip & Virtual Environment

### What is pip?
pip is the package installer for Python. It allows you to install packages from PyPI (Python Package Index).

### Installing Packages
```bash
# Install a package
pip install package_name

# Install specific version
pip install package_name==1.2.3

# Install with version constraint
pip install package_name>=1.0,<2.0

# Install multiple packages
pip install package1 package2 package3

# Install from requirements file
pip install -r requirements.txt
```

### Managing Packages
```bash
# List installed packages
pip list

# Show package information
pip show package_name

# Upgrade package
pip install --upgrade package_name

# Uninstall package
pip uninstall package_name

# Create requirements file
pip freeze > requirements.txt
```

### Virtual Environment

#### Why Virtual Environment?
- Isolate project dependencies
- Avoid version conflicts
- Easy to reproduce environment
- Keep system Python clean

#### Creating Virtual Environment

**On Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

#### Using Virtual Environment
```bash
# Check which Python is active
which python  # macOS/Linux
where python  # Windows

# Install packages (only in this environment)
pip install flask

# Check installed packages
pip list

# Deactivate virtual environment
deactivate
```

#### requirements.txt
```
flask==2.3.0
requests==2.31.0
numpy==1.24.0
pandas==2.0.0
```

#### Setting up Project
```bash
# Create project directory
mkdir my_project
cd my_project

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Work on project...

# Deactivate when done
deactivate
```

### Poetry (Alternative)
Poetry is a modern dependency management tool.

```bash
# Install poetry
pip install poetry

# Create new project
poetry new my_project

# Initialize poetry in existing project
poetry init

# Add dependency
poetry add flask

# Install dependencies from lock file
poetry install

# Run command in virtual environment
poetry run python script.py

# Deactivate
exit
```

---

## Practice Exercises

### Exercise 1: Create a Calculator Package
Create a `calculator` package with modules for basic operations, advanced operations, and geometry.

### Exercise 2: Create a Configuration Module
Create a module to handle application configuration with functions to load, save, and validate settings.

### Exercise 3: Use External Packages
1. Create a virtual environment
2. Install `requests` and `beautifulsoup4`
3. Write a script that fetches a webpage and parses it

### Exercise 4: Create a Utility Package
Create a `utils` package with modules for:
- File operations
- String manipulation
- Data validation

---

## Key Takeaways
✅ Modules organize code in single files  
✅ Packages organize code in directories  
✅ Virtual environments isolate project dependencies  
✅ pip manages third-party packages  
✅ __all__ defines public API  
✅ Use requirements.txt for reproducibility  

---

## Next Steps
→ Learn about [Advanced Python](../11_Advanced_Python/README.md)
