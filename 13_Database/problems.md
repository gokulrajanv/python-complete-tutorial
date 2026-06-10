# 13 - DATABASE - PRACTICE PROBLEMS

## 🟢 Beginner Level Problems

### Problem 1: Create Table
**Difficulty:** 🟢 Easy  
**Time:** 5 minutes

Create a simple SQLite table.

**Solution:**
```python
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

conn.commit()
conn.close()
print("Table created!")
```

---

### Problem 2: Insert Data
**Difficulty:** 🟢 Easy  
**Time:** 5 minutes

Insert records into table.

**Solution:**
```python
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))

conn.commit()
conn.close()
print("Data inserted!")
```

---

## 🟡 Intermediate Level Problems

### Problem 3: Query Data
**Difficulty:** 🟡 Medium  
**Time:** 10 minutes

Retrieve and display data.

**Solution:**
```python
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM users WHERE age > 25")
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

conn.close()
```

---

## 🔴 Advanced Level Problems

### Problem 4: Update and Delete
**Difficulty:** 🔴 Hard  
**Time:** 15 minutes

Perform CRUD operations.

**Solution:**
```python
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Update
cursor.execute("UPDATE users SET age = 26 WHERE name = 'Alice'")

# Delete
cursor.execute("DELETE FROM users WHERE name = 'Bob'")

# Query result
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.commit()
conn.close()
```

---

**Good Luck! Master databases! 🚀**
