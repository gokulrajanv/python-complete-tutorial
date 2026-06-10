# 16 - TESTING - PRACTICE PROBLEMS

## 🟢 Beginner Level Problems

### Problem 1: Simple Unit Test
**Difficulty:** 🟢 Easy  
**Time:** 5 minutes

Write a basic unit test.

**Solution:**
```python
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)

if __name__ == '__main__':
    unittest.main()
```

---

### Problem 2: Test Multiple Cases
**Difficulty:** 🟢 Easy  
**Time:** 5 minutes

Test various scenarios.

**Solution:**
```python
import unittest

def multiply(a, b):
    return a * b

class TestMultiply(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(multiply(3, 4), 12)
    
    def test_negative(self):
        self.assertEqual(multiply(-3, 4), -12)
    
    def test_zero(self):
        self.assertEqual(multiply(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
```

---

## 🟡 Intermediate Level Problems

### Problem 3: Test String Functions
**Difficulty:** 🟡 Medium  
**Time:** 10 minutes

Test string manipulation.

**Solution:**
```python
import unittest

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

class TestStrings(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_string("hello"), "olleh")
    
    def test_palindrome_true(self):
        self.assertTrue(is_palindrome("racecar"))
    
    def test_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))

if __name__ == '__main__':
    unittest.main()
```

---

## 🔴 Advanced Level Problems

### Problem 4: Test with Exceptions
**Difficulty:** 🔴 Hard  
**Time:** 15 minutes

Test error handling.

**Solution:**
```python
import unittest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestDivide(unittest.TestCase):
    def test_normal_division(self):
        self.assertEqual(divide(10, 2), 5)
    
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

---

**Good Luck! Master testing! 🚀**
