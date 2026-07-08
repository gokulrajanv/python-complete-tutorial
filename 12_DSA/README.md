# 1️⃣2️⃣ Data Structures & Algorithms - Complete Guide

Master Arrays, Linked Lists, Stacks, Queues, Sorting, Searching, and Time Complexity.

## Table of Contents

1. [Arrays & Lists](#arrays--lists)
2. [Linked Lists](#linked-lists)
3. [Stacks](#stacks)
4. [Queues](#queues)
5. [Searching Algorithms](#searching-algorithms)
6. [Sorting Algorithms](#sorting-algorithms)
7. [Time Complexity](#time-complexity)

---

## 🟢 Arrays & Lists

### Python List Operations

```python
# Create array
arr = [1, 2, 3, 4, 5]

# Access elements
print(arr[0])    # 1
print(arr[-1])   # 5

# Slicing
print(arr[1:3])  # [2, 3]
print(arr[:3])   # [1, 2, 3]
print(arr[2:])   # [3, 4, 5]

# Operations
arr.append(6)     # Add at end
arr.insert(0, 0)  # Add at start
arr.remove(3)     # Remove value
arr.pop(0)        # Remove by index
```

### 2D Arrays (Matrix)

```python
# Create 2D array
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access elements
print(matrix[0][0])   # 1
print(matrix[1][2])   # 6

# Iterate
for row in matrix:
    for elem in row:
        print(elem, end=" ")
```

---

## 🟡 Linked Lists

### Node Class

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### Linked List Implementation

```python
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def delete(self, data):
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))
```

---

## 🟡 Stacks

### Stack using List

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    
    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # 3
print(stack.peek())  # 2
```

### Balanced Parentheses

```python
def is_balanced(expression):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    
    return stack.is_empty()
```

---

## 🟡 Queues

### Queue using List

```python
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None
    
    def front(self):
        return self.items[0] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # 1
print(queue.front())    # 2
```

---

## 🟡 Searching Algorithms

### Linear Search

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Time: O(n)
print(linear_search([1, 2, 3, 4, 5], 3))  # 2
```

### Binary Search

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Time: O(log n)
print(binary_search([1, 2, 3, 4, 5], 3))  # 2
```

---

## 🟡 Sorting Algorithms

### Bubble Sort

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Time: O(n²)
print(bubble_sort([5, 2, 8, 1, 9]))  # [1, 2, 5, 8, 9]
```

### Quick Sort

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

# Time: O(n log n) average
print(quick_sort([5, 2, 8, 1, 9]))  # [1, 2, 5, 8, 9]
```

### Merge Sort

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Time: O(n log n)
print(merge_sort([5, 2, 8, 1, 9]))  # [1, 2, 5, 8, 9]
```

---

## 🔴 Time Complexity

### Big O Notation

```
O(1)     - Constant time
O(log n) - Logarithmic
O(n)     - Linear
O(n log n) - Linearithmic
O(n²)    - Quadratic
O(n³)    - Cubic
O(2ⁿ)    - Exponential
O(n!)    - Factorial
```

### Examples

```python
# O(1) - Constant
def get_first(arr):
    return arr[0]

# O(n) - Linear
def linear_search(arr, target):
    for elem in arr:
        if elem == target:
            return True
    return False

# O(n²) - Quadratic
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# O(log n) - Logarithmic
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
```

### Complexity Comparison

| Algorithm | Best | Average | Worst |
|-----------|------|---------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Linear Search | O(1) | O(n) | O(n) |
| Binary Search | O(1) | O(log n) | O(log n) |

---

## 📝 Summary

| Data Structure | Insert | Delete | Search | Space |
|---|---|---|---|---|
| Array | O(n) | O(n) | O(n) | O(n) |
| Linked List | O(1) | O(1) | O(n) | O(n) |
| Stack | O(1) | O(1) | O(n) | O(n) |
| Queue | O(1) | O(1) | O(n) | O(n) |

---

**Next:** [13_Database](../13_Database/README.md) →
