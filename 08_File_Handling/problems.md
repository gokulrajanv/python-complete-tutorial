# 08 - File Handling Practice Problems

## 🟢 Beginner Problems

### Problem 1: Write and Read File
Create a file called "greetings.txt" with 3 lines of text, then read and print the content.

```python
# Your code here
```

**Expected Output:**
```
(Content of the file you wrote)
```

---

### Problem 2: Append to File
Create a file with initial content, then append 2 more lines to it.

```python
# Your code here
```

---

### Problem 3: Count Lines
Write a function that counts the number of lines in a file.

```python
def count_lines(filename):
    # Your code here
    pass

# Test it
print(count_lines("test.txt"))
```

---

### Problem 4: Read CSV File
Given a CSV file with student data, read and print each student's information.

```python
# Create CSV first
import csv
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Grade"])
    writer.writerow(["Alice", 20, "A"])
    writer.writerow(["Bob", 21, "B"])

# Your code here to read and print
```

---

### Problem 5: Write JSON File
Create a Python dictionary and save it as a JSON file with proper formatting.

```python
import json

person = {"name": "Alice", "age": 25, "city": "NYC"}

# Your code here
```

---

## 🟡 Intermediate Problems

### Problem 6: Read JSON File
Read a JSON file and print all the data in a formatted way.

```python
import json

# Your code here
```

---

### Problem 7: File Statistics
Write a function that returns statistics about a file:
- Number of lines
- Number of words
- Number of characters

```python
def file_statistics(filename):
    # Your code here
    pass

stats = file_statistics("data.txt")
print(f"Lines: {stats['lines']}, Words: {stats['words']}, Characters: {stats['characters']}")
```

---

### Problem 8: Search in File
Write a function that searches for a word in a file and returns the line numbers where it appears.

```python
def search_word(filename, word):
    # Your code here
    pass

results = search_word("data.txt", "python")
print(results)
```

**Expected Output:**
```
[1, 3, 5]  # Line numbers
```

---

### Problem 9: Copy File
Write a function that copies the content of one file to another.

```python
def copy_file(source, destination):
    # Your code here
    pass

copy_file("original.txt", "copy.txt")
```

---

### Problem 10: Filter CSV
Given a CSV file with student data, filter and write only students with grade "A" to a new file.

```python
import csv

def filter_csv(input_file, output_file, column, value):
    # Your code here
    pass

filter_csv("students.csv", "top_students.csv", "Grade", "A")
```

---

### Problem 11: Merge Multiple Files
Write a function that merges multiple text files into one.

```python
def merge_files(input_files, output_file):
    # Your code here
    pass

merge_files(["file1.txt", "file2.txt", "file3.txt"], "merged.txt")
```

---

### Problem 12: Word Frequency
Given a text file, create a dictionary with word frequencies and save it as JSON.

```python
import json

def word_frequency(filename):
    # Your code here
    pass

freq = word_frequency("data.txt")
with open("frequency.json", "w") as f:
    json.dump(freq, f, indent=4)
```

---

## 🔴 Advanced Problems

### Problem 13: CSV to JSON Converter
Write a function that converts a CSV file to JSON format.

```python
import csv
import json

def csv_to_json(csv_file, json_file):
    # Your code here
    pass

csv_to_json("students.csv", "students.json")
```

---

### Problem 14: JSON to CSV Converter
Write a function that converts a JSON file (list of dictionaries) to CSV format.

```python
import json
import csv

def json_to_csv(json_file, csv_file):
    # Your code here
    pass

json_to_csv("students.json", "students.csv")
```

---

### Problem 15: Process Large File
Write a function that processes a large file line by line without loading it entirely into memory.

```python
def process_large_file(filename, processor_func):
    # Your code here
    pass

def uppercase_processor(line):
    return line.upper()

process_large_file("large.txt", uppercase_processor)
```

---

### Problem 16: File Backup System
Create a function that automatically backs up a file with a timestamp in the filename.

```python
import os
from datetime import datetime

def backup_file(filename):
    # Your code here
    pass

backup_file("important.txt")
# Should create: important_2024-01-15_14-30-45.txt
```

---

### Problem 17: Remove Duplicates
Given a CSV file with potentially duplicate rows, write a new CSV with duplicates removed.

```python
import csv

def remove_csv_duplicates(input_file, output_file):
    # Your code here
    pass

remove_csv_duplicates("data.csv", "cleaned.csv")
```

---

### Problem 18: Data Aggregation
Given a CSV with sales data (Date, Product, Amount), create a summary JSON by product.

```python
import csv
import json

def aggregate_sales(csv_file, json_file):
    # Your code here
    pass

aggregate_sales("sales.csv", "summary.json")
# Output should be like: {"product_name": {"total": 1000, "count": 5, "average": 200}}
```

---

### Problem 19: File Difference Analyzer
Write a function that compares two files line by line and shows the differences.

```python
def compare_files(file1, file2):
    # Your code here
    pass

differences = compare_files("original.txt", "modified.txt")
for diff in differences:
    print(diff)
```

---

### Problem 20: Batch File Processor
Write a function that processes all .txt files in a directory (e.g., convert to uppercase, count words).

```python
import os

def batch_process(directory, operation):
    # Your code here
    pass

def count_words(filepath):
    with open(filepath, 'r') as f:
        return len(f.read().split())

batch_process("./text_files", count_words)
```

---

## Solutions

Check the `solutions.py` file for detailed solutions to all problems.
