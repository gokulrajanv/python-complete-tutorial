# ===================================
# 12 - Data Structures & Algorithms Examples
# ===================================

# ===== LINKED LIST =====
print("\n=== LINKED LIST ===")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_beginning(0)
ll.display()  # 0 -> 1 -> 2 -> 3

# ===== STACK =====
print("\n=== STACK ===")

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

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"Peek: {stack.peek()}")  # 3
print(f"Pop: {stack.pop()}")    # 3
print(f"Peek: {stack.peek()}")  # 2

# ===== QUEUE =====
print("\n=== QUEUE ===")

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(f"Dequeue: {queue.dequeue()}")  # 1
print(f"Dequeue: {queue.dequeue()}")  # 2

# ===== SEARCHING =====
print("\n=== SEARCHING ===")

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

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

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Linear search 5: {linear_search(arr, 5)}")
print(f"Binary search 5: {binary_search(arr, 5)}")
print(f"Binary search 7: {binary_search(arr, 7)}")

# ===== SORTING =====
print("\n=== SORTING ===")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

arr1 = [5, 2, 8, 1, 9, 3]
arr2 = [5, 2, 8, 1, 9, 3]

print(f"Bubble sort: {bubble_sort(arr1)}")
print(f"Quick sort: {quick_sort(arr2)}")

# ===== MERGE SORT =====
print("\n=== MERGE SORT ===")

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

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

arr3 = [5, 2, 8, 1, 9, 3, 7, 4]
print(f"Merge sort: {merge_sort(arr3)}")

print("\nDone!")
