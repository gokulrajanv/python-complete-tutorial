# 5️⃣ Collections - Complete Guide

Master Lists, Tuples, Sets, and Dictionaries with comprehensions and advanced operations.

## Table of Contents

1. [Lists](#lists)
2. [List Comprehension](#list-comprehension)
3. [Tuples](#tuples)
4. [Sets](#sets)
5. [Dictionaries](#dictionaries)
6. [Dictionary Comprehension](#dictionary-comprehension)

---

## 🟢 Lists

### Creating Lists

```python
# Empty list
empty_list = []

# List with elements
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

# List with range
range_list = list(range(1, 6))  # [1, 2, 3, 4, 5]
```

### Accessing Elements

```python
fruits = ["apple", "banana", "cherry", "date"]

# Positive indexing
print(fruits[0])    # apple
print(fruits[2])    # cherry

# Negative indexing
print(fruits[-1])   # date
print(fruits[-2])   # cherry

# Slicing
print(fruits[1:3])   # ['banana', 'cherry']
print(fruits[:2])    # ['apple', 'banana']
print(fruits[2:])    # ['cherry', 'date']
print(fruits[::2])   # ['apple', 'cherry'] (every 2nd)
```

### List Methods

```python
fruits = ["apple", "banana"]

# append() - add element at end
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# insert() - add element at specific index
fruits.insert(1, "blueberry")
print(fruits)  # ['apple', 'blueberry', 'banana', 'cherry']

# remove() - remove first occurrence
fruits.remove("banana")
print(fruits)  # ['apple', 'blueberry', 'cherry']

# pop() - remove by index
fruits.pop(0)  # removes 'apple'
print(fruits)  # ['blueberry', 'cherry']

# clear() - remove all
fruits.clear()
print(fruits)  # []

# extend() - add multiple elements
fruits = ["apple", "banana"]
fruits.extend(["cherry", "date"])
print(fruits)  # ['apple', 'banana', 'cherry', 'date']

# index() - find index of element
numbers = [10, 20, 30, 20]
print(numbers.index(20))  # 1 (first occurrence)

# count() - count occurrences
print(numbers.count(20))  # 2

# sort() - sort list
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)  # [1, 1, 3, 4, 5]

# reverse() - reverse list
numbers.reverse()
print(numbers)  # [5, 4, 3, 1, 1]
```

### List Operations

```python
# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  # [1, 2, 3, 4, 5, 6]

# Repetition
list3 = ["x"] * 3
print(list3)  # ['x', 'x', 'x']

# Membership
print(5 in [1, 2, 3, 4, 5])  # True
print(10 in [1, 2, 3, 4, 5])  # False

# Length
print(len([1, 2, 3, 4, 5]))  # 5
```

---

## 🟡 List Comprehension

### Basic Syntax

```python
# Regular way
squares = []
for x in range(5):
    squares.append(x ** 2)
print(squares)  # [0, 1, 4, 9, 16]

# List comprehension way
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

### With Conditions

```python
# Even numbers only
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Odd numbers squared
odd_squares = [x ** 2 for x in range(10) if x % 2 != 0]
print(odd_squares)  # [1, 9, 25, 49, 81]
```

### Nested List Comprehension

```python
# Matrix (2D list)
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Flattening a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [x for row in matrix for x in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 🟢 Tuples

### Creating Tuples

```python
# Empty tuple
empty_tuple = ()

# Tuple with elements
numbers = (1, 2, 3, 4, 5)
fruits = ("apple", "banana", "cherry")
mixed = (1, "hello", 3.14, True)

# Single element tuple (note the comma)
single = (42,)
print(type(single))  # <class 'tuple'>

# Without parentheses
auto_tuple = 1, 2, 3
print(auto_tuple)  # (1, 2, 3)
```

### Tuple Operations

```python
fruits = ("apple", "banana", "cherry")

# Indexing and slicing (same as lists)
print(fruits[0])     # apple
print(fruits[-1])    # cherry
print(fruits[1:])    # ('banana', 'cherry')

# Unpacking
a, b, c = fruits
print(a, b, c)  # apple banana cherry

# count() and index()
print(numbers.count(2))    # 1
print(numbers.index(3))    # 2

# Immutability (tuples cannot be changed)
# fruits[0] = "orange"  # ERROR!
```

### Tuple vs List

```python
# Tuples are immutable (cannot change)
# Tuples are faster and use less memory
# Tuples can be used as dictionary keys

dict_with_tuple_key = {(1, 2): "coordinate"}
print(dict_with_tuple_key[(1, 2)])  # coordinate

# Lists cannot be dictionary keys
# dict_with_list_key = {[1, 2]: "coordinate"}  # ERROR!
```

---

## 🟡 Sets

### Creating Sets

```python
# Empty set (note: {} is a dict, not a set!)
empty_set = set()

# Set with elements
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}
mixed = {1, "hello", 3.14}

# From list (removes duplicates)
from_list = set([1, 2, 2, 3, 3, 3])
print(from_list)  # {1, 2, 3}
```

### Set Operations

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union (all elements)
print(set1 | set2)          # {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.union(set2))     # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection (common elements)
print(set1 & set2)          # {4, 5}
print(set1.intersection(set2))  # {4, 5}

# Difference (in set1 but not set2)
print(set1 - set2)          # {1, 2, 3}
print(set1.difference(set2))  # {1, 2, 3}

# Symmetric difference (in either but not both)
print(set1 ^ set2)          # {1, 2, 3, 6, 7, 8}
print(set1.symmetric_difference(set2))  # {1, 2, 3, 6, 7, 8}
```

### Set Methods

```python
fruits = {"apple", "banana"}

# add() - add single element
fruits.add("cherry")
print(fruits)  # {'apple', 'banana', 'cherry'}

# update() - add multiple elements
fruits.update(["date", "elderberry"])
print(fruits)  # {'apple', 'banana', 'cherry', 'date', 'elderberry'}

# remove() - remove element (error if not found)
fruits.remove("apple")
print(fruits)  # {'banana', 'cherry', 'date', 'elderberry'}

# discard() - remove element (no error if not found)
fruits.discard("orange")  # No error

# pop() - remove random element
fruits.pop()

# clear() - remove all
fruits.clear()
print(fruits)  # set()
```

### Set Membership

```python
numbers = {1, 2, 3, 4, 5}

print(3 in numbers)   # True
print(10 in numbers)  # False
print(10 not in numbers)  # True
print(len(numbers))   # 5
```

---

## 🟡 Dictionaries

### Creating Dictionaries

```python
# Empty dictionary
empty_dict = {}
empty_dict2 = dict()

# Dictionary with key-value pairs
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC",
    "is_student": True
}

# Using dict() constructor
person2 = dict(name="Bob", age=30, city="LA")
```

### Accessing Dictionary Values

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Using square brackets
print(person["name"])      # Alice
print(person["age"])       # 25

# Using get() method (safer)
print(person.get("name"))         # Alice
print(person.get("country"))      # None
print(person.get("country", "Unknown"))  # Unknown (default value)
```

### Dictionary Methods

```python
person = {"name": "Alice", "age": 25}

# keys() - get all keys
print(person.keys())       # dict_keys(['name', 'age'])
print(list(person.keys())) # ['name', 'age']

# values() - get all values
print(person.values())     # dict_values(['Alice', 25])
print(list(person.values()))  # ['Alice', 25]

# items() - get key-value pairs
print(person.items())      # dict_items([('name', 'Alice'), ('age', 25)])
for key, value in person.items():
    print(f"{key}: {value}")

# update() - add/update items
person.update({"city": "NYC", "country": "USA"})
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'NYC', 'country': 'USA'}

# pop() - remove item
age = person.pop("age")
print(age)     # 25
print(person)  # {'name': 'Alice', 'city': 'NYC', 'country': 'USA'}

# popitem() - remove last item
person.popitem()

# clear() - remove all
person.clear()
print(person)  # {}
```

### Nested Dictionaries

```python
student = {
    "name": "Alice",
    "address": {
        "street": "123 Main St",
        "city": "NYC",
        "zip": "10001"
    },
    "grades": {
        "math": 95,
        "english": 88,
        "science": 92
    }
}

print(student["address"]["city"])  # NYC
print(student["grades"]["math"])   # 95
```

### Iterating Over Dictionary

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Iterate over keys
for key in person:
    print(key, person[key])

# Iterate over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

# Iterate over values only
for value in person.values():
    print(value)
```

---

## 🔴 Dictionary Comprehension

### Basic Syntax

```python
# Regular way
squares = {}
for x in range(5):
    squares[x] = x ** 2
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Dictionary comprehension way
squares = {x: x ** 2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### With Conditions

```python
# Only even numbers
evens = {x: x ** 2 for x in range(10) if x % 2 == 0}
print(evens)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Convert list to dictionary
fruits = ["apple", "banana", "cherry"]
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(fruit_lengths)  # {'apple': 5, 'banana': 6, 'cherry': 6}
```

### Swapping Keys and Values

```python
person = {"name": "Alice", "age": "25", "city": "NYC"}
swapped = {v: k for k, v in person.items()}
print(swapped)  # {'Alice': 'name', '25': 'age', 'NYC': 'city'}
```

---

## 📝 Summary

| Collection | Mutable | Ordered | Allows Duplicates | Use Case |
|------------|---------|---------|-------------------|-----------|
| List | ✅ | ✅ | ✅ | Flexible collection with order |
| Tuple | ❌ | ✅ | ✅ | Immutable sequences |
| Set | ✅ | ❌ | ❌ | Unique values, fast lookup |
| Dictionary | ✅ | ✅ (3.7+) | N/A | Key-value pairs |

---

**Next:** [06_Functions](../06_Functions/README.md) →
