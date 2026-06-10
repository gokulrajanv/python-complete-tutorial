# 🗄️ 13 - DATABASE

## Introduction to Databases

Learn to work with databases using SQL and Python.

---

## 📚 Table of Contents
1. [SQLite](#sqlite)
2. [SQL Basics](#sql-basics)
3. [Python sqlite3](#python-sqlite3)

---

## SQLite

### Lightweight Database

SQLite is a file-based database perfect for learning and small projects.

---

## SQL Basics

### CREATE

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);
```

### INSERT

```sql
INSERT INTO users (name, age) VALUES ('Alice', 25);
```

### SELECT

```sql
SELECT * FROM users WHERE age > 20;
```

### UPDATE

```sql
UPDATE users SET age = 26 WHERE name = 'Alice';
```

### DELETE

```sql
DELETE FROM users WHERE name = 'Alice';
```

---

## Python sqlite3

### Connect to Database

```python
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
```

### Create Table

```python
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')
conn.commit()
```

### Insert Data

```python
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
conn.commit()
```

### Fetch Data

```python
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
```

---

## 🎯 Key Takeaways

- ✅ Use SQLite for learning
- ✅ Master basic SQL
- ✅ Use Python sqlite3 module
- ✅ Always commit changes

---

**Ready to practice? Check `problems.md` for exercises!** 🚀
