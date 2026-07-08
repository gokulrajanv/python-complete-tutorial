# ===================================
# 08 - File Handling Examples
# ===================================

import os
import json
import csv

print("\n=== FILE HANDLING EXAMPLES ===")

# ===== WRITING FILES =====
print("\n--- Writing Files ---")

# Write a simple text file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2\n")
    file.write("This is line 3")

print("Created example.txt")

# ===== READING FILES =====
print("\n--- Reading Files ---")

# Read entire file
with open("example.txt", "r") as file:
    content = file.read()
    print("Content:")
    print(content)

# Read line by line
print("\nLine by line:")
with open("example.txt", "r") as file:
    for line in file:
        print(f"  {line.strip()}")

# ===== APPENDING FILES =====
print("\n--- Appending Files ---")

with open("example.txt", "a") as file:
    file.write("\nThis line was appended")

print("Appended to example.txt")

# ===== FILE OPERATIONS =====
print("\n--- File Operations ---")

# Check if file exists
if os.path.exists("example.txt"):
    print("example.txt exists")
    size = os.path.getsize("example.txt")
    print(f"File size: {size} bytes")

# List files in current directory
print("\nPython files in current directory:")
py_files = [f for f in os.listdir(".") if f.endswith(".py")]
for py_file in py_files[:5]:  # Show first 5
    print(f"  {py_file}")

# ===== CSV FILES =====
print("\n--- CSV Files ---")

# Write CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Grade"])
    writer.writerow(["Alice", 20, "A"])
    writer.writerow(["Bob", 21, "B"])
    writer.writerow(["Charlie", 19, "A"])

print("Created students.csv")

# Read CSV
print("\nReading students.csv:")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"  {row}")

# Read CSV as Dictionary
print("\nReading CSV as Dictionary:")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"  {row['Name']}: {row['Age']} years old, Grade: {row['Grade']}")

# ===== JSON FILES =====
print("\n--- JSON Files ---")

# Create data
students_data = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 21, "grade": "B"},
    {"name": "Charlie", "age": 19, "grade": "A"}
]

# Write JSON
with open("students.json", "w") as file:
    json.dump(students_data, file, indent=4)

print("Created students.json")

# Read JSON
print("\nReading students.json:")
with open("students.json", "r") as file:
    data = json.load(file)
    for student in data:
        print(f"  {student['name']}: Age {student['age']}, Grade {student['grade']}")

# JSON string operations
print("\n--- JSON String Operations ---")
person = {"name": "Diana", "age": 22, "city": "NYC"}
json_string = json.dumps(person, indent=2)
print("JSON String:")
print(json_string)

parsed = json.loads(json_string)
print(f"\nParsed back: {parsed}")

# ===== PRACTICAL EXAMPLE: WORD COUNT =====
print("\n--- Practical Example: Word Count ---")

# Create a sample file
with open("sample.txt", "w") as file:
    file.write("Python is great. Python is powerful. Python is fun.")

# Count word occurrences
with open("sample.txt", "r") as file:
    text = file.read()
    words = text.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

print("Word count:")
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  {word}: {count}")

# ===== CLEANUP =====
print("\n--- Cleanup ---")
for file in ["example.txt", "students.csv", "students.json", "sample.txt"]:
    if os.path.exists(file):
        os.remove(file)
        print(f"Deleted {file}")

print("\nDone!")
