# Strings - Practice Problems

## 🟢 Beginner Level

### Problem 1: String Length and Indexing
Find the length and access specific characters.

**Solution:**
```python
text = input("Enter text: ")
print(f"Length: {len(text)}")
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
```

---

### Problem 2: Case Conversion
Convert string to different cases.

**Solution:**
```python
text = input("Enter text: ")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Title: {text.title()}")
```

---

### Problem 3: Count Character
Count occurrences of a character.

**Solution:**
```python
text = input("Enter text: ")
char = input("Character to count: ")
print(f"'{char}' appears {text.count(char)} times")
```

---

### Problem 4: Reverse String
Reverse a string.

**Solution:**
```python
text = input("Enter text: ")
reversed_text = text[::-1]
print(f"Reversed: {reversed_text}")
```

---

### Problem 5: Check Palindrome
Check if a string is a palindrome.

**Solution:**
```python
text = input("Enter text: ").lower()
if text == text[::-1]:
    print("Palindrome!")
else:
    print("Not a palindrome")
```

---

## 🟡 Intermediate Level

### Problem 6: String Slicing
Extract substrings.

**Solution:**
```python
text = "Hello World Python"
print(f"First 5: {text[:5]}")
print(f"Last 6: {text[-6:]}")
print(f"Middle: {text[6:11]}")
```

---

### Problem 7: Find and Replace
Find and replace text.

**Solution:**
```python
text = "Hello World"
find_text = input("Find: ")
replace_text = input("Replace with: ")
result = text.replace(find_text, replace_text)
print(f"Result: {result}")
```

---

### Problem 8: Word Frequency
Count word frequency in text.

**Solution:**
```python
text = input("Enter text: ").lower()
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word}: {count}")
```

---

### Problem 9: Email Validation (Simple)
Check if email contains @.

**Solution:**
```python
email = input("Enter email: ")
if "@" in email and "." in email:
    print("Valid email format")
else:
    print("Invalid email")
```

---

### Problem 10: Split and Join
Split and rejoin strings.

**Solution:**
```python
text = "apple,banana,cherry"
items = text.split(",")
result = " | ".join(items)
print(f"Result: {result}")
```

---

## 🔴 Advanced Level

### Problem 11: Remove Duplicates
Remove duplicate characters.

**Solution:**
```python
text = input("Enter text: ")
result = ""
for char in text:
    if char not in result:
        result += char
print(f"No duplicates: {result}")

# Alternative using dict
result2 = "".join(dict.fromkeys(text))
print(f"Alternative: {result2}")
```

---

### Problem 12: Anagram Check
Check if two strings are anagrams.

**Solution:**
```python
text1 = input("Text 1: ").lower().replace(" ", "")
text2 = input("Text 2: ").lower().replace(" ", "")

if sorted(text1) == sorted(text2):
    print("Anagrams!")
else:
    print("Not anagrams")
```

---

### Problem 13: Regex - Phone Validation
Validate phone number format.

**Solution:**
```python
import re

phone = input("Enter phone: ")
pattern = r"^\d{3}-\d{3}-\d{4}$"

if re.match(pattern, phone):
    print("Valid phone number")
else:
    print("Invalid format (expected: XXX-XXX-XXXX)")
```

---

### Problem 14: Regex - Extract Emails
Extract all emails from text.

**Solution:**
```python
import re

text = "Contact: john@example.com or jane@test.org"
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(pattern, text)
print(f"Emails found: {emails}")
```

---

### Problem 15: String Compression
Compress consecutive characters.

**Solution:**
```python
text = "aaabbccccdd"
result = ""
count = 1

for i in range(len(text)):
    if i + 1 < len(text) and text[i] == text[i + 1]:
        count += 1
    else:
        result += text[i] + str(count)
        count = 1

print(f"Original: {text}")
print(f"Compressed: {result}")
```

---

## 📊 Problem Summary

| # | Problem | Level |
|---|---------|-------|
| 1 | Length & Indexing | 🟢 |
| 2 | Case Conversion | 🟢 |
| 3 | Count Character | 🟢 |
| 4 | Reverse String | 🟢 |
| 5 | Palindrome Check | 🟢 |
| 6 | String Slicing | 🟡 |
| 7 | Find & Replace | 🟡 |
| 8 | Word Frequency | 🟡 |
| 9 | Email Validation | 🟡 |
| 10 | Split & Join | 🟡 |
| 11 | Remove Duplicates | 🔴 |
| 12 | Anagram Check | 🔴 |
| 13 | Regex Phone | 🔴 |
| 14 | Extract Emails | 🔴 |
| 15 | String Compression | 🔴 |

---

**Keep Practicing! 🚀**
