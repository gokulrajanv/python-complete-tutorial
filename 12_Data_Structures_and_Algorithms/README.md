# 12. Data Structures & Algorithms

## Overview
Data structures and algorithms are fundamental to computer science. This section covers arrays, linked lists, stacks, queues, searching, sorting, and time complexity analysis.

## Table of Contents
1. [Arrays & Linked Lists](#arrays--linked-lists)
2. [Stack & Queue](#stack--queue)
3. [Searching & Sorting](#searching--sorting)
4. [Time Complexity](#time-complexity)

---

## Arrays & Linked Lists

### Arrays (Lists in Python)
Arrays store elements sequentially in memory.

```python
# Creating arrays
arr = [1, 2, 3, 4, 5]
arr = list(range(5))  # [0, 1, 2, 3, 4]

# Accessing elements
print(arr[0])      # 1
print(arr[-1])     # Last element

# Array operations
arr.append(6)      # Add to end
arr.insert(2, 10)  # Insert at index
arr.remove(10)     # Remove by value
arr.pop()          # Remove last element
arr.pop(0)         # Remove at index

# Array slicing
print(arr[1:3])    # Elements from index 1 to 2
print(arr[:3])     # First 3 elements
print(arr[::2])    # Every second element

# Searching in array
print(3 in arr)    # True/False
print(arr.index(3))  # Index of element

# Array length and sum
print(len(arr))
print(sum(arr))
```

### Linked Lists
A linked list stores elements in nodes, where each node points to the next.

```python
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if current is None:
                return
            current = current.next
        
        new_node.next = current.next
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
    
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

# Using LinkedList
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # 1 -> 2 -> 3

ll.insert_at_beginning(0)
ll.display()  # 0 -> 1 -> 2 -> 3

ll.delete(2)
ll.display()  # 0 -> 1 -> 3

print(ll.search(1))  # True
```

---

## Stack & Queue

### Stack (LIFO - Last In First Out)
```python
# Stack using list
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Using Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())   # 3
print(stack.peek())  # 2
print(stack.size())  # 2

# Stack application: Balanced parentheses
def is_balanced(s):
    stack = Stack()
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:
            stack.push(char)
        elif char in pairs.values():
            if stack.is_empty() or pairs[stack.pop()] != char:
                return False
    
    return stack.is_empty()

print(is_balanced("({[]})"))  # True
print(is_balanced("({[}])"))  # False
```

### Queue (FIFO - First In First Out)
```python
from collections import deque

# Queue using deque
class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, data):
        self.items.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Using Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # 1
print(queue.front())    # 2
print(queue.size())     # 2
```

---

## Searching & Sorting

### Searching Algorithms

#### Linear Search
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search([3, 1, 4, 1, 5], 4))  # 2
```

#### Binary Search
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

print(binary_search([1, 3, 5, 7, 9], 7))  # 3
```

### Sorting Algorithms

#### Bubble Sort
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort([64, 34, 25, 12, 22]))  # [12, 22, 25, 34, 64]
```

#### Selection Sort
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([64, 34, 25, 12, 22]))  # [12, 22, 25, 34, 64]
```

#### Insertion Sort
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort([64, 34, 25, 12, 22]))  # [12, 22, 25, 34, 64]
```

#### Quick Sort
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([64, 34, 25, 12, 22]))  # [12, 22, 25, 34, 64]
```

#### Merge Sort
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

print(merge_sort([64, 34, 25, 12, 22]))  # [12, 22, 25, 34, 64]
```

---

## Time Complexity

### Understanding Big O Notation
Big O notation describes how an algorithm's performance scales with input size.

```python
# O(1) - Constant Time
def get_first(arr):
    return arr[0]

# O(n) - Linear Time
def linear_search(arr, target):
    for i in arr:
        if i == target:
            return True
    return False

# O(n²) - Quadratic Time
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# O(log n) - Logarithmic Time
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

# O(n log n) - Linearithmic Time
def merge_sort(arr):
    # See merge sort implementation above
    pass
```

### Complexity Comparison Table
| Notation | Time | Example |
|----------|------|---------|
| O(1) | Constant | Array indexing |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search |
| O(n log n) | Linearithmic | Merge sort, Quick sort |
| O(n²) | Quadratic | Bubble sort, Insertion sort |
| O(n³) | Cubic | Triple nested loop |
| O(2ⁿ) | Exponential | Recursive algorithms |
| O(n!) | Factorial | Generating permutations |

---

## Practice Exercises

### Exercise 1: Implement Doubly Linked List
Create a doubly linked list with insertion, deletion, and display methods.

### Exercise 2: Stack Application
Implement a function to evaluate postfix expressions using a stack.

### Exercise 3: Queue Application
Implement breadth-first search (BFS) for a graph using a queue.

### Exercise 4: Sorting Comparison
Compare execution times of different sorting algorithms on large datasets.

---

## Key Takeaways
✅ Arrays provide fast random access  
✅ Linked lists provide efficient insertion/deletion  
✅ Stacks follow LIFO principle  
✅ Queues follow FIFO principle  
✅ Binary search is faster than linear search for sorted data  
✅ Big O notation helps analyze algorithm efficiency  

---

## Next Steps
→ Learn about [Database](../13_Database/README.md)
