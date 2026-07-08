# 05 - Collections Practice Problems

## 🟢 Beginner Problems

### Problem 1: List Operations
Create a list of 10 numbers. Find:
- The maximum number
- The minimum number
- The sum of all numbers
- The average

```python
numbers = [5, 12, 8, 23, 6, 14, 9, 18, 3, 11]

# Your code here
```

**Expected Output:**
```
Maximum: 23
Minimum: 3
Sum: 109
Average: 10.9
```

---

### Problem 2: List Manipulation
Given a list of fruits, perform these operations:
- Add "mango" at the end
- Insert "blueberry" at position 2
- Remove "banana"
- Print the final list

```python
fruits = ["apple", "banana", "cherry"]

# Your code here
```

**Expected Output:**
```
['apple', 'blueberry', 'cherry', 'mango']
```

---

### Problem 3: List Comprehension
Create a list of squares for numbers from 1 to 10 using list comprehension.

```python
# Your code here
print(squares)
```

**Expected Output:**
```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

---

### Problem 4: Tuple Unpacking
Given a tuple of 3 values, unpack them into separate variables and print each.

```python
data = ("Alice", 25, "NYC")

# Your code here
```

**Expected Output:**
```
Name: Alice
Age: 25
City: NYC
```

---

### Problem 5: Set Operations
Given two sets, find and print:
- Common elements (intersection)
- All elements (union)
- Elements in set1 but not in set2

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Your code here
```

**Expected Output:**
```
Common: {4, 5}
All: {1, 2, 3, 4, 5, 6, 7, 8}
Difference: {1, 2, 3}
```

---

### Problem 6: Dictionary Creation
Create a dictionary with 5 key-value pairs representing a person's information:
- name
- age
- email
- city
- is_student

Then print each key-value pair.

```python
# Your code here
```

---

### Problem 7: Dictionary Access
Given a dictionary, retrieve values using both bracket notation and .get() method, including a default value for a missing key.

```python
person = {"name": "Bob", "age": 30, "city": "LA"}

# Your code here
```

**Expected Output:**
```
Name (bracket): Bob
Age (bracket): 30
Country (bracket method with default): Unknown
```

---

## 🟡 Intermediate Problems

### Problem 8: Filter Even Numbers
Use list comprehension to create a list containing only even numbers from 1 to 50.

```python
# Your code here
print(evens)
```

**Expected Output:**
```
[2, 4, 6, 8, ..., 48, 50]
```

---

### Problem 9: Nested List Comprehension
Create a 3x3 matrix (nested list) using list comprehension where each element is the product of its row and column indices.

```python
# Your code here
for row in matrix:
    print(row)
```

**Expected Output:**
```
[0, 0, 0]
[0, 1, 2]
[0, 2, 4]
```

---

### Problem 10: Remove Duplicates
Given a list with duplicate values, remove duplicates while preserving order.

```python
original = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]

# Your code here
print(unique)
```

**Expected Output:**
```
[1, 2, 3, 4, 5]
```

---

### Problem 11: Dictionary from List
Given a list of words, create a dictionary where keys are words and values are their lengths.

```python
words = ["python", "programming", "is", "fun"]

# Your code here
print(word_lengths)
```

**Expected Output:**
```
{'python': 6, 'programming': 11, 'is': 2, 'fun': 3}
```

---

### Problem 12: Count Occurrences
Create a dictionary that counts occurrences of each character in a string.

```python
text = "hello world"

# Your code here
print(char_count)
```

**Expected Output:**
```
{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

---

### Problem 13: Sort Dictionary by Values
Given a dictionary with student names and scores, sort by scores in descending order.

```python
students = {"Alice": 85, "Bob": 90, "Charlie": 78, "Diana": 92}

# Your code here
for name, score in sorted_students:
    print(f"{name}: {score}")
```

**Expected Output:**
```
Diana: 92
Bob: 90
Alice: 85
Charlie: 78
```

---

### Problem 14: Nested Dictionary Traversal
Given a nested dictionary, find and print the math grade of a student.

```python
school = {
    "students": [
        {"name": "Alice", "grades": {"math": 95, "english": 88}},
        {"name": "Bob", "grades": {"math": 87, "english": 92}}
    ]
}

# Your code here - find Alice's math grade
```

**Expected Output:**
```
Alice's math grade: 95
```

---

## 🔴 Advanced Problems

### Problem 15: Complex List Comprehension
Create a list of tuples containing (number, square, cube) for numbers 1-10 where the number is divisible by 2 or 3.

```python
# Your code here
for item in result:
    print(item)
```

**Expected Output:**
```
(2, 4, 8)
(3, 9, 27)
(4, 16, 64)
(6, 36, 216)
...
```

---

### Problem 16: Set Operations with Conditions
Given three sets, find elements that are in set1 and set2 but not in set3.

```python
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {5, 6, 7, 8, 9}

# Your code here
print(result)
```

**Expected Output:**
```
{3, 4}
```

---

### Problem 17: Transpose a Matrix
Given a 2D list (matrix), create its transpose (swap rows and columns).

```python
matrix = [[1, 2, 3], [4, 5, 6]]

# Your code here
for row in transposed:
    print(row)
```

**Expected Output:**
```
[1, 4]
[2, 5]
[3, 6]
```

---

### Problem 18: Dictionary Merge
Merge two dictionaries. If there are conflicting keys, values from dict2 should override dict1.

```python
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"c": 30, "d": 4, "e": 5}

# Your code here
print(merged)
```

**Expected Output:**
```
{'a': 1, 'b': 2, 'c': 30, 'd': 4, 'e': 5}
```

---

### Problem 19: Group by Category
Given a list of items with categories, create a dictionary grouping items by category.

```python
items = [
    {"name": "apple", "category": "fruit"},
    {"name": "carrot", "category": "vegetable"},
    {"name": "banana", "category": "fruit"},
    {"name": "potato", "category": "vegetable"}
]

# Your code here
print(grouped)
```

**Expected Output:**
```
{
    'fruit': ['apple', 'banana'],
    'vegetable': ['carrot', 'potato']
}
```

---

### Problem 20: Find Duplicates
Given a list, return another list containing all duplicate values.

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]

# Your code here
print(duplicates)
```

**Expected Output:**
```
[2, 3, 4]
```

---

## Solutions

Check the `solutions.py` file for detailed solutions to all problems.
