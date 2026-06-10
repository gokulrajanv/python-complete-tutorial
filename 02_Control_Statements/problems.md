# Control Statements - Practice Problems

## 🟢 Beginner Level

### Problem 1: Age Classification
**Difficulty:** 🟢 Beginner

Classify a person based on age:
- Child: < 13
- Teenager: 13-19
- Adult: 20-59
- Senior: 60+

**Solution:**
```python
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")
```

---

### Problem 2: Even or Odd
**Difficulty:** 🟢 Beginner

Check if a number is even or odd.

**Solution:**
```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
```

---

### Problem 3: Largest of Three Numbers
**Difficulty:** 🟢 Beginner

Find the largest among three numbers.

**Solution:**
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print(f"Largest: {a}")
elif b > a and b > c:
    print(f"Largest: {b}")
else:
    print(f"Largest: {c}")

# Alternative (simpler)
largest = max(a, b, c)
print(f"Largest: {largest}")
```

---

### Problem 4: Login System
**Difficulty:** 🟢 Beginner

Validate username and password.

**Solution:**
```python
username = input("Username: ")
password = input("Password: ")

correct_user = "admin"
correct_pass = "admin123"

if username == correct_user and password == correct_pass:
    print("✓ Login successful")
else:
    print("✗ Invalid credentials")
```

---

### Problem 5: Voting Eligibility
**Difficulty:** 🟢 Beginner

Check if someone can vote (age >= 18).

**Solution:**
```python
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to vote")
else:
    years_to_wait = 18 - age
    print(f"Not eligible. Wait {years_to_wait} more years")
```

---

## 🟡 Intermediate Level

### Problem 6: Grade Assignment
**Difficulty:** 🟡 Intermediate

Assign grades based on score:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Below 60: F

**Solution:**
```python
score = int(input("Enter score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")
```

---

### Problem 7: BMI Category
**Difficulty:** 🟡 Intermediate

Categorize BMI (weight / height²):
- < 18.5: Underweight
- 18.5-24.9: Normal
- 25-29.9: Overweight
- ≥ 30: Obese

**Solution:**
```python
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi:.2f}, Category: {category}")
```

---

### Problem 8: Discount Calculator
**Difficulty:** 🟡 Intermediate

Calculate discount based on purchase amount:
- ≤ 500: No discount
- 501-1000: 5%
- 1001-5000: 10%
- > 5000: 15%

**Solution:**
```python
amount = float(input("Purchase amount: $"))

if amount <= 500:
    discount = 0
elif amount <= 1000:
    discount = amount * 0.05
elif amount <= 5000:
    discount = amount * 0.10
else:
    discount = amount * 0.15

final = amount - discount
print(f"Original: ${amount}")
print(f"Discount: ${discount}")
print(f"Final: ${final}")
```

---

### Problem 9: Day Type Classification
**Difficulty:** 🟡 Intermediate

Classify day (1-7) as weekday or weekend.

**Solution:**
```python
day = int(input("Enter day number (1-7): "))

if day == 1 or day == 7:
    day_type = "Weekend"
elif 2 <= day <= 6:
    day_type = "Weekday"
else:
    day_type = "Invalid"

print(f"Day {day}: {day_type}")
```

---

### Problem 10: Leap Year Checker
**Difficulty:** 🟡 Intermediate

Check if a year is a leap year:
- Divisible by 400 → Leap
- Divisible by 100 → Not leap
- Divisible by 4 → Leap
- Otherwise → Not leap

**Solution:**
```python
year = int(input("Enter year: "))

if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False

if is_leap:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```

---

## 🔴 Advanced Level

### Problem 11: Complex Eligibility Check
**Difficulty:** 🔴 Advanced

Check multiple conditions:
- Age >= 18 AND
- Income >= $30,000 AND
- Credit score >= 650
- Output: "Approved", "Pending Review", or "Rejected"

**Solution:**
```python
age = int(input("Age: "))
income = float(input("Income: $"))
credit_score = int(input("Credit Score: "))

if age >= 18:
    if income >= 30000:
        if credit_score >= 650:
            status = "Approved"
        elif credit_score >= 600:
            status = "Pending Review"
        else:
            status = "Rejected (Low credit)"
    else:
        status = "Rejected (Low income)"
else:
    status = "Rejected (Too young)"

print(f"Application Status: {status}")
```

---

### Problem 12: Number Classification
**Difficulty:** 🔴 Advanced

Classify a number as:
- Positive/Negative
- Even/Odd
- Prime/Composite (if applicable)

**Solution:**
```python
num = int(input("Enter number: "))

# Positive/Negative
sign = "Positive" if num > 0 else ("Negative" if num < 0 else "Zero")

# Even/Odd
parity = "Even" if num % 2 == 0 else "Odd"

# Prime check (for positive numbers)
is_prime = False
if num > 1:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

print(f"{num}: {sign}, {parity}")
if num > 0:
    print(f"Prime: {'Yes' if is_prime else 'No'}")
```

---

### Problem 13: Ternary Chain
**Difficulty:** 🔴 Advanced

Use nested ternary operators.

**Solution:**
```python
score = int(input("Score: "))

# Nested ternary (readable version)
grade = (
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "F"
)

print(f"Grade: {grade}")
```

---

### Problem 14: Complex Business Logic
**Difficulty:** 🔴 Advanced

Shipping cost calculation with multiple conditions:
- Base cost: $10
- Weight surcharge: $2 per kg
- Distance surcharge: $0.50 per mile
- Member discount: 10%
- Expedited: +$15

**Solution:**
```python
weight = float(input("Weight (kg): "))
distance = float(input("Distance (miles): "))
is_member = input("Member? (yes/no): ").lower() == "yes"
expedited = input("Expedited? (yes/no): ").lower() == "yes"

# Calculate base cost
cost = 10
cost += weight * 2
cost += distance * 0.5

# Add expedited fee
if expedited:
    cost += 15

# Apply member discount
if is_member:
    cost *= 0.9

print(f"Shipping cost: ${cost:.2f}")
```

---

### Problem 15: Match-Case Advanced
**Difficulty:** 🔴 Advanced

Use match-case for pattern matching.

**Solution:**
```python
# Requires Python 3.10+
command = input("Enter command (start/stop/restart/status): ").lower()

match command:
    case "start":
        print("Starting service...")
    case "stop":
        print("Stopping service...")
    case "restart":
        print("Restarting service...")
    case "status":
        print("Service is running")
    case _:
        print("Unknown command")
```

---

## 📊 Problem Summary

| # | Problem | Level |
|---|---------|-------|
| 1 | Age Classification | 🟢 |
| 2 | Even or Odd | 🟢 |
| 3 | Largest of Three | 🟢 |
| 4 | Login System | 🟢 |
| 5 | Voting Eligibility | 🟢 |
| 6 | Grade Assignment | 🟡 |
| 7 | BMI Category | 🟡 |
| 8 | Discount Calculator | 🟡 |
| 9 | Day Type | 🟡 |
| 10 | Leap Year | 🟡 |
| 11 | Complex Eligibility | 🔴 |
| 12 | Number Classification | 🔴 |
| 13 | Ternary Chain | 🔴 |
| 14 | Business Logic | 🔴 |
| 15 | Match-Case Advanced | 🔴 |

---

**Keep Practicing! 🚀**
