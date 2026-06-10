# 07 - EXCEPTION HANDLING - PRACTICE PROBLEMS

## 🟢 Beginner Level Problems

### Problem 1: Simple Try-Except
**Difficulty:** 🟢 Easy  
**Time:** 5 minutes

Write a program that divides two numbers and handles division by zero.

**Solution:**
```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
```

---

### Problem 2: Convert String to Integer
**Difficulty:** 🟢 Easy  
**Time:** 5 minutes

Get user input and convert to integer, handling invalid input.

**Solution:**
```python
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("Error: Please enter a valid number!")
```

---

### Problem 3: List Index Error
**Difficulty:** 🟢 Easy  
**Time:** 5 minutes

Access list items safely.

**Solution:**
```python
numbers = [1, 2, 3]
try:
    index = int(input("Enter index: "))
    print(numbers[index])
except IndexError:
    print("Error: Index out of range!")
except ValueError:
    print("Error: Enter a valid number!")
```

---

## 🟡 Intermediate Level Problems

### Problem 4: Multiple Exception Types
**Difficulty:** 🟡 Medium  
**Time:** 10 minutes

Handle multiple exception types in calculator.

**Solution:**
```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")
    
    if op == "+":
        result = a + b
    elif op == "/":
        result = a / b
    else:
        result = "Invalid operator"
    
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input!")
```

---

### Problem 5: Finally Block
**Difficulty:** 🟡 Medium  
**Time:** 10 minutes

Use finally to perform cleanup.

**Solution:**
```python
try:
    file = open("data.txt", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found!")
finally:
    print("File handling complete!")
    if 'file' in locals():
        file.close()
```

---

## 🔴 Advanced Level Problems

### Problem 6: Custom Exception
**Difficulty:** 🔴 Hard  
**Time:** 15 minutes

Create and raise custom exception.

**Solution:**
```python
class NegativeNumberError(Exception):
    pass

def validate_age(age):
    if age < 0:
        raise NegativeNumberError("Age cannot be negative!")
    if age > 120:
        raise ValueError("Age is unrealistic!")
    return age

try:
    age = int(input("Enter age: "))
    valid_age = validate_age(age)
    print(f"Valid age: {valid_age}")
except NegativeNumberError as e:
    print(f"Custom Error: {e}")
except ValueError as e:
    print(f"Value Error: {e}")
```

---

**Good Luck! Master exception handling! 🚀**
