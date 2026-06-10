# 🐍 01 - PYTHON BASICS

## Introduction to Python

Python is a simple, elegant, and powerful programming language that's perfect for beginners. It reads almost like English!

---

## 📚 Table of Contents
1. [What is Python?](#what-is-python)
2. [Setup & Installation](#setup--installation)
3. [Your First Program](#your-first-program)
4. [Variables & Data Types](#variables--data-types)
5. [Operators](#operators)
6. [Input & Output](#input--output)
7. [Comments](#comments)

---

## What is Python?

Python is a high-level programming language that emphasizes **code readability** and **simplicity**.

### Why Learn Python?
- ✅ Easy to learn - clear syntax
- ✅ Versatile - web, data science, AI, automation
- ✅ Large community - lots of resources
- ✅ In-demand - top job skill
- ✅ Powerful libraries - Django, NumPy, Pandas, etc.

---

## Setup & Installation

### Windows
1. Visit https://www.python.org/downloads/
2. Download Python 3.x
3. Run installer
4. ✅ Check "Add Python to PATH"
5. Click Install

### Mac
```bash
brew install python3
```

### Linux
```bash
sudo apt-get install python3
```

### Verify Installation
```bash
python --version
# or
python3 --version
```

---

## Your First Program

### Hello World!
```python
print("Hello, World!")
```

**Output:**
```
Hello, World!
```

That's it! You just wrote your first Python program! 🎉

---

## Variables & Data Types

### What is a Variable?
A variable is a named container that stores a value.

```python
# Create variables
name = "Alice"
age = 25
height = 5.6
is_student = True

# Use variables
print(name)        # Alice
print(age)         # 25
print(height)      # 5.6
print(is_student)  # True
```

### Main Data Types

#### 1. **String** (Text)
```python
greeting = "Hello, Python!"
name = 'John'
message = """This is a
multi-line string"""

print(greeting)    # Hello, Python!
print(len(name))   # 4 (length)
```

#### 2. **Integer** (Whole Numbers)
```python
age = 25
count = 100
negative = -50

print(age + 10)    # 35
print(count * 2)   # 200
```

#### 3. **Float** (Decimal Numbers)
```python
price = 19.99
temperature = -5.5
pi = 3.14159

print(price + 5.01)    # 25.0
print(temperature * 2)  # -11.0
```

#### 4. **Boolean** (True/False)
```python
is_raining = True
is_sunny = False
is_adult = age >= 18

print(is_raining)   # True
print(is_sunny)     # False
print(is_adult)     # True (if age >= 18)
```

### Check Data Type
```python
value = 42
print(type(value))  # <class 'int'>

value = 3.14
print(type(value))  # <class 'float'>

value = "Hello"
print(type(value))  # <class 'str'>

value = True
print(type(value))  # <class 'bool'>
```

---

## Operators

### 1. **Arithmetic Operators**
```python
a = 10
b = 3

print(a + b)    # 13 (addition)
print(a - b)    # 7 (subtraction)
print(a * b)    # 30 (multiplication)
print(a / b)    # 3.333... (division)
print(a // b)   # 3 (floor division)
print(a % b)    # 1 (modulus/remainder)
print(a ** b)   # 1000 (exponent)
```

### 2. **Comparison Operators**
```python
a = 10
b = 5

print(a > b)    # True (greater than)
print(a < b)    # False (less than)
print(a >= b)   # True (greater than or equal)
print(a <= b)   # False (less than or equal)
print(a == b)   # False (equal to)
print(a != b)   # True (not equal)
```

### 3. **Logical Operators**
```python
is_raining = True
is_cold = False

print(is_raining and is_cold)  # False (both must be true)
print(is_raining or is_cold)   # True (at least one is true)
print(not is_raining)          # False (reverses boolean)
```

### 4. **Assignment Operators**
```python
x = 10          # assign
x += 5          # x = x + 5 (15)
x -= 3          # x = x - 3 (12)
x *= 2          # x = x * 2 (24)
x /= 4          # x = x / 4 (6.0)
```

---

## Input & Output

### Output - `print()`
```python
# Simple print
print("Hello")              # Hello

# Multiple items
print("Name:", "Alice")     # Name: Alice

# Formatting
print("I have", 5, "apples")  # I have 5 apples

# Special characters
print("Line 1\nLine 2")    # Line break
print("Tab\tSeparated")    # Tab
```

### Input - `input()`
```python
# Get user input (always returns string)
name = input("Enter your name: ")
print("Hello,", name)

# Convert to other types
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
```

### Example: Simple Program
```python
# Get user information
name = input("What is your name? ")
age = int(input("What is your age? "))
city = input("What city do you live in? ")

# Display information
print("\n--- Your Information ---")
print("Name:", name)
print("Age:", age)
print("City:", city)
```

---

## Comments

Comments are notes in your code that Python ignores.

### Single-line Comments
```python
# This is a comment
print("Hello")  # This is also a comment
```

### Multi-line Comments
```python
"""
This is a multi-line comment.
It can span multiple lines.
Use it for longer explanations.
"""
print("Code here")
```

---

## 🎯 Key Takeaways

- ✅ Variables store values
- ✅ Python has main data types: str, int, float, bool
- ✅ Use operators to perform calculations
- ✅ `print()` displays output
- ✅ `input()` gets user input
- ✅ Comments explain your code

---

## 📖 Next Steps

1. Run the examples
2. Modify them and experiment
3. Solve the practice problems
4. Move to Section 02 - Control Statements

---

## 🔗 Resources

- Python Official Docs: https://docs.python.org/3/
- Python Tutorial: https://realpython.com/python-basics/
- Built-in Functions: https://docs.python.org/3/library/functions.html

---

**Ready to practice? Check `problems.md` for exercises!** 🚀
