# ===================================
# 05 - Collections Examples
# ===================================

# ===== LISTS =====
print("\n=== LISTS ===")
fruits = ["apple", "banana", "cherry", "date"]
print("Original list:", fruits)
print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("Slice [1:3]:", fruits[1:3])

fruits.append("elderberry")
print("After append:", fruits)

fruits.insert(2, "blueberry")
print("After insert:", fruits)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("Original numbers:", numbers)
print("Count of 1:", numbers.count(1))
print("Index of 4:", numbers.index(4))
numbers.sort()
print("After sort:", numbers)

# ===== LIST COMPREHENSION =====
print("\n=== LIST COMPREHENSION ===")
squares = [x ** 2 for x in range(6)]
print("Squares:", squares)

evens = [x for x in range(20) if x % 2 == 0]
print("Even numbers (0-19):", evens)

odd_squares = [x ** 2 for x in range(10) if x % 2 != 0]
print("Odd squares:", odd_squares)

matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Matrix:")
for row in matrix:
    print(row)

flattened = [x for row in matrix for x in row]
print("Flattened:", flattened)

# ===== TUPLES =====
print("\n=== TUPLES ===")
coordinates = (10, 20, 30)
print("Tuple:", coordinates)
print("Type:", type(coordinates))
x, y, z = coordinates
print("Unpacked:", x, y, z)

data = (1, 2, 2, 3, 3, 3, 4)
print("Count of 3:", data.count(3))
print("Index of 2:", data.index(2))

# ===== SETS =====
print("\n=== SETS ===")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (1-2):", set1 - set2)
print("Symmetric difference:", set1 ^ set2)

fruits_set = {"apple", "banana"}
fruits_set.add("cherry")
print("After add:", fruits_set)

fruits_set.update(["date", "elderberry"])
print("After update:", fruits_set)

fruits_set.remove("apple")
print("After remove:", fruits_set)

# Remove duplicates from list
duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = set(duplicates)
print("Unique from list:", unique)

# ===== DICTIONARIES =====
print("\n=== DICTIONARIES ===")
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC",
    "is_student": True
}

print("Person:", person)
print("Name:", person["name"])
print("Age:", person.get("age"))
print("Country (with default):", person.get("country", "Unknown"))

print("\nKeys:", list(person.keys()))
print("Values:", list(person.values()))

person["email"] = "alice@example.com"
print("After adding email:", person)

person.update({"age": 26, "city": "LA"})
print("After update:", person)

for key, value in person.items():
    print(f"  {key}: {value}")

# Nested dictionary
student = {
    "name": "Bob",
    "address": {
        "street": "123 Main St",
        "city": "Boston"
    },
    "grades": {
        "math": 95,
        "english": 88
    }
}

print("\nNested Dictionary:")
print("Name:", student["name"])
print("City:", student["address"]["city"])
print("Math grade:", student["grades"]["math"])

# ===== DICTIONARY COMPREHENSION =====
print("\n=== DICTIONARY COMPREHENSION ===")
squares_dict = {x: x ** 2 for x in range(6)}
print("Squares dict:", squares_dict)

evens_dict = {x: x ** 2 for x in range(10) if x % 2 == 0}
print("Evens dict:", evens_dict)

fruits_list = ["apple", "banana", "cherry"]
fruit_lengths = {fruit: len(fruit) for fruit in fruits_list}
print("Fruit lengths:", fruit_lengths)

original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print("Original:", original)
print("Swapped:", swapped)

# ===== MIXED OPERATIONS =====
print("\n=== MIXED OPERATIONS ===")
# Convert between collections
my_list = [1, 2, 2, 3, 3, 3]
my_set = set(my_list)
my_tuple = tuple(my_set)
my_list_again = list(my_tuple)

print("List:", my_list)
print("Set:", my_set)
print("Tuple:", my_tuple)
print("Back to list:", my_list_again)
