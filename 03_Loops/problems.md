# Loops - Practice Problems

## 🟢 Beginner Level

### Problem 1: Print Numbers 1-10
Print numbers from 1 to 10 using a for loop.

**Solution:**
```python
for i in range(1, 11):
    print(i)
```

---

### Problem 2: Sum of Numbers
Calculate the sum of numbers from 1 to 100.

**Solution:**
```python
total = 0
for i in range(1, 101):
    total += i
print(f"Sum: {total}")
```

---

### Problem 3: Print Multiplication Table
Print the multiplication table of 5 (1-10).

**Solution:**
```python
for i in range(1, 11):
    print(f"5 × {i} = {5 * i}")
```

---

### Problem 4: Count to 5 with while
Use while loop to count from 1 to 5.

**Solution:**
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

---

### Problem 5: Print Even Numbers
Print all even numbers from 1 to 20.

**Solution:**
```python
for i in range(2, 21, 2):
    print(i)
```

---

## 🟡 Intermediate Level

### Problem 6: Factorial Calculation
Calculate factorial of a number using a loop.

**Solution:**
```python
n = int(input("Enter number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")
```

---

### Problem 7: Reverse a Number
Reverse a number using a loop.

**Solution:**
```python
num = int(input("Enter number: "))
reversed_num = 0
temp = num

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

print(f"Reversed: {reversed_num}")
```

---

### Problem 8: Count Occurrences
Count occurrences of a character in a string.

**Solution:**
```python
text = input("Enter text: ")
char = input("Character to count: ")

count = 0
for c in text:
    if c == char:
        count += 1

print(f"'{char}' appears {count} times")
```

---

### Problem 9: Print Pyramid
Print a pyramid pattern with asterisks.

**Solution:**
```python
n = 5
for i in range(1, n + 1):
    print("*" * i)
```

---

### Problem 10: Break Example - Search
Find a number in a list and break.

**Solution:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search = 6

for num in numbers:
    if num == search:
        print(f"Found {search}")
        break
```

---

## 🔴 Advanced Level

### Problem 11: Nested Loops - Times Table
Create a 5×5 times table.

**Solution:**
```python
print("Times Table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")
    print()
```

---

### Problem 12: Diamond Pattern
Print a diamond pattern.

**Solution:**
```python
n = 4
# Upper half
for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

# Lower half
for i in range(n - 1, 0, -1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
```

---

### Problem 13: Prime Numbers
Find all prime numbers from 2 to 50.

**Solution:**
```python
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()
```

---

### Problem 14: Sum of Digits
Calculate sum of digits in a number.

**Solution:**
```python
num = int(input("Enter number: "))
digit_sum = 0

for digit in str(num):
    digit_sum += int(digit)

print(f"Sum of digits: {digit_sum}")
```

---

### Problem 15: Continue Example - Skip Multiples
Print numbers 1-20 but skip multiples of 3.

**Solution:**
```python
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()
```

---

## 📊 Problem Summary

| # | Problem | Level |
|---|---------|-------|
| 1 | Print 1-10 | 🟢 |
| 2 | Sum 1-100 | 🟢 |
| 3 | Multiplication Table | 🟢 |
| 4 | Count with while | 🟢 |
| 5 | Even Numbers | 🟢 |
| 6 | Factorial | 🟡 |
| 7 | Reverse Number | 🟡 |
| 8 | Count Occurrences | 🟡 |
| 9 | Pyramid | 🟡 |
| 10 | Break Example | 🟡 |
| 11 | Times Table | 🔴 |
| 12 | Diamond Pattern | 🔴 |
| 13 | Prime Numbers | 🔴 |
| 14 | Sum of Digits | 🔴 |
| 15 | Continue Example | 🔴 |

---

**Keep Practicing! 🚀**
