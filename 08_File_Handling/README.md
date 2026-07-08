# 8️⃣ File Handling - Complete Guide

Master reading, writing, and manipulating files including CSV and JSON formats.

## Table of Contents

1. [File Basics](#file-basics)
2. [Reading Files](#reading-files)
3. [Writing Files](#writing-files)
4. [File Operations](#file-operations)
5. [CSV Files](#csv-files)
6. [JSON Files](#json-files)

---

## 🟢 File Basics

### Opening Files

```python
# Basic syntax
file = open("filename.txt", "mode")

# File modes:
# "r"  - Read (default, file must exist)
# "w"  - Write (creates new file, overwrites if exists)
# "a"  - Append (adds to end of file)
# "x"  - Create (creates new file, error if exists)
# "b"  - Binary mode (rb, wb, etc.)
# "+"  - Read and write (r+, w+, a+)
```

### The with Statement (Best Practice)

```python
# Using 'with' automatically closes the file
with open("file.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here
```

---

## 🟢 Reading Files

### read() - Read Entire File

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

### readline() - Read One Line

```python
with open("data.txt", "r") as file:
    line1 = file.readline()  # Includes \n
    line2 = file.readline()
    print(line1.strip())  # Remove newline
    print(line2.strip())
```

### readlines() - Read All Lines

```python
with open("data.txt", "r") as file:
    lines = file.readlines()  # List of lines
    for line in lines:
        print(line.strip())
```

### Iterate Over File

```python
with open("data.txt", "r") as file:
    for line in file:  # Most memory-efficient
        print(line.strip())
```

### Read Specific Number of Characters

```python
with open("data.txt", "r") as file:
    first_10_chars = file.read(10)
    print(first_10_chars)
```

---

## 🟡 Writing Files

### write() - Write to File

```python
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2\n")
    file.write("This is line 3")
```

### writelines() - Write Multiple Lines

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

### Append Mode

```python
# Append to existing file
with open("output.txt", "a") as file:
    file.write("New line at the end\n")
```

### Writing with Formatting

```python
with open("output.txt", "w") as file:
    file.write(f"Name: Alice\nAge: 25\nCity: NYC")
```

---

## 🟡 File Operations

### Check if File Exists

```python
import os

if os.path.exists("file.txt"):
    print("File exists")
else:
    print("File does not exist")
```

### Get File Information

```python
import os

filename = "data.txt"

if os.path.isfile(filename):
    size = os.path.getsize(filename)  # Size in bytes
    print(f"File size: {size} bytes")

if os.path.isdir("folder"):
    print("It's a directory")
```

### List Files in Directory

```python
import os

files = os.listdir(".")
for file in files:
    print(file)
```

### Rename File

```python
import os

os.rename("old_name.txt", "new_name.txt")
```

### Delete File

```python
import os

if os.path.exists("file.txt"):
    os.remove("file.txt")
    print("File deleted")
```

### Create Directory

```python
import os

if not os.path.exists("my_folder"):
    os.mkdir("my_folder")
    print("Directory created")
```

### List Python Files in Directory

```python
import os

python_files = [f for f in os.listdir(".") if f.endswith(".py")]
print(python_files)
```

---

## 🟡 CSV Files

### Reading CSV

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list
```

### Reading CSV as Dictionary

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)  # Uses first row as keys
    for row in reader:
        print(row)  # Each row is a dict
        print(row["name"], row["age"])
```

### Writing CSV

```python
import csv

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])  # Header
    writer.writerow(["Alice", 25, "NYC"])
    writer.writerow(["Bob", 30, "LA"])
```

### Writing CSV as Dictionary

```python
import csv

with open("output.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 25, "city": "NYC"})
    writer.writerow({"name": "Bob", "age": 30, "city": "LA"})
```

---

## 🟡 JSON Files

### Reading JSON

```python
import json

with open("data.json", "r") as file:
    data = json.load(file)  # Converts JSON to Python dict/list
    print(data)
    print(data["name"])
```

### Writing JSON

```python
import json

data = {
    "name": "Alice",
    "age": 25,
    "city": "NYC",
    "hobbies": ["reading", "coding", "gaming"]
}

with open("output.json", "w") as file:
    json.dump(data, file, indent=4)  # indent for pretty printing
```

### JSON String Operations

```python
import json

# Convert Python object to JSON string
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data, indent=2)
print(json_string)

# Convert JSON string to Python object
json_str = '{"name": "Bob", "age": 30}'
parsed_data = json.loads(json_str)
print(parsed_data["name"])
```

### Pretty Print JSON

```python
import json

data = {
    "name": "Alice",
    "age": 25,
    "address": {
        "street": "123 Main St",
        "city": "NYC"
    },
    "hobbies": ["reading", "coding"]
}

json_string = json.dumps(data, indent=4, sort_keys=True)
print(json_string)
```

---

## 🔴 Advanced File Operations

### Read Large Files Efficiently

```python
def read_large_file(filename, chunk_size=1024):
    with open(filename, "r") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            process(chunk)

def process(data):
    print(f"Processing {len(data)} characters")

read_large_file("large_file.txt")
```

### Backup File

```python
import shutil
import os

def backup_file(filename):
    if os.path.exists(filename):
        backup_name = f"{filename}.backup"
        shutil.copy(filename, backup_name)
        print(f"Backup created: {backup_name}")

backup_file("important.txt")
```

### Compare Two Files

```python
def compare_files(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        content1 = f1.read()
        content2 = f2.read()
        return content1 == content2

if compare_files("file1.txt", "file2.txt"):
    print("Files are identical")
else:
    print("Files are different")
```

### Search in File

```python
def search_in_file(filename, search_term):
    found = False
    with open(filename, "r") as file:
        for line_num, line in enumerate(file, 1):
            if search_term in line:
                print(f"Found at line {line_num}: {line.strip()}")
                found = True
    if not found:
        print(f"'{search_term}' not found in file")

search_in_file("data.txt", "python")
```

### Count Lines in File

```python
def count_lines(filename):
    with open(filename, "r") as file:
        return sum(1 for line in file)

lines = count_lines("data.txt")
print(f"Total lines: {lines}")
```

---

## 📝 Summary

| Operation | Method | Example |
|-----------|--------|----------|
| Read entire | `read()` | `file.read()` |
| Read line | `readline()` | `file.readline()` |
| Read all lines | `readlines()` | `file.readlines()` |
| Write | `write()` | `file.write(text)` |
| Append | `append mode` | `open(file, "a")` |
| Check exists | `os.path.exists()` | `os.path.exists(file)` |
| Delete | `os.remove()` | `os.remove(file)` |
| CSV read | `csv.reader()` | `csv.reader(file)` |
| JSON read | `json.load()` | `json.load(file)` |
| JSON write | `json.dump()` | `json.dump(data, file)` |

---

**Next:** [09_OOP](../09_OOP/README.md) →
