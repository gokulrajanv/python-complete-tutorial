# 12 - Data Structures & Algorithms Practice Problems

## 🟢 Beginner Problems

### Problem 1: Array Basics
Given an array, find the maximum and minimum elements.

```python
arr = [3, 7, 2, 9, 1, 5]

# Your code here
```

**Expected Output:**
```
Maximum: 9
Minimum: 1
```

---

### Problem 2: Linear Search
Implement linear search to find if a number exists in an array.

```python
def linear_search(arr, target):
    # Your code here
    pass

print(linear_search([1, 2, 3, 4, 5], 3))  # True
print(linear_search([1, 2, 3, 4, 5], 10))  # False
```

---

### Problem 3: Bubble Sort
Implement bubble sort algorithm.

```python
def bubble_sort(arr):
    # Your code here
    pass

print(bubble_sort([5, 2, 8, 1, 9]))  # [1, 2, 5, 8, 9]
```

---

### Problem 4: Stack Implementation
Implement a basic stack with push, pop, and peek operations.

```python
class Stack:
    # Your code here
    pass

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())   # 2
print(stack.peek())  # 1
```

---

### Problem 5: Queue Implementation
Implement a basic queue with enqueue and dequeue operations.

```python
class Queue:
    # Your code here
    pass

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # 1
```

---

## 🟡 Intermediate Problems

### Problem 6: Binary Search
Implement binary search (array must be sorted).

```python
def binary_search(arr, target):
    # Your code here
    pass

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))  # 6 (index)
```

---

### Problem 7: Linked List Implementation
Implement a basic linked list with insert and delete.

```python
class Node:
    # Your code here
    pass

class LinkedList:
    # Your code here
    pass

ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.display()  # 1 -> 2
```

---

### Problem 8: Quick Sort
Implement quick sort algorithm.

```python
def quick_sort(arr):
    # Your code here
    pass

print(quick_sort([5, 2, 8, 1, 9]))  # [1, 2, 5, 8, 9]
```

---

### Problem 9: Reverse Array
Reverse an array without using built-in reverse().

```python
def reverse_array(arr):
    # Your code here
    pass

print(reverse_array([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
```

---

### Problem 10: Count Occurrences
Count how many times a number appears in an array.

```python
def count_occurrences(arr, target):
    # Your code here
    pass

print(count_occurrences([1, 2, 2, 3, 3, 3, 4], 3))  # 3
```

---

## 🔴 Advanced Problems

### Problem 11: Merge Sort
Implement merge sort algorithm.

```python
def merge_sort(arr):
    # Your code here
    pass

print(merge_sort([5, 2, 8, 1, 9]))  # [1, 2, 5, 8, 9]
```

---

### Problem 12: Balanced Parentheses
Use stack to check if parentheses are balanced.

```python
def is_balanced(expression):
    # Your code here
    pass

print(is_balanced("(())"))      # True
print(is_balanced("(())"))      # True
print(is_balanced("(())"))      # False
```

---

### Problem 13: Find Missing Number
Given array of n-1 numbers from 1 to n, find the missing one.

```python
def find_missing(arr):
    # Your code here
    pass

print(find_missing([1, 2, 4, 5]))  # 3
```

---

### Problem 14: Two Sum
Find two numbers that add up to a target sum.

```python
def two_sum(arr, target):
    # Your code here
    pass

print(two_sum([1, 2, 3, 4, 5], 7))  # (2, 5) or (3, 4)
```

---

### Problem 15: 2D Matrix Search
Search for a value in a 2D matrix.

```python
def search_2d(matrix, target):
    # Your code here
    pass

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(search_2d(matrix, 5))  # True
```

---

## Solutions

Check the `solutions.py` file for detailed solutions.
