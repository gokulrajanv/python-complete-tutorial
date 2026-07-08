# 15 - APIs Practice Problems

## 🟢 Beginner Problems

### Problem 1: Simple GET Request
Make a GET request to JSONPlaceholder API and print user information.

```python
import requests

response = requests.get('https://jsonplaceholder.typicode.com/users/1')

# Your code here
```

**Expected Output:**
```
Name: Leanne Graham
Email: Bret@april.biz
City: Gwenborough
```

---

### Problem 2: Get Request with Parameters
Make a GET request with query parameters.

```python
import requests

params = {'userId': 1, '_limit': 5}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)

# Your code here
```

---

### Problem 3: Check Response Status
Make a request and check the status code.

```python
import requests

response = requests.get('https://jsonplaceholder.typicode.com/users/1')

if response.status_code == 200:
    print("Success")
else:
    print("Error")
```

---

### Problem 4: JSON Response
Make a request and parse JSON response.

```python
import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
data = response.json()

# Your code here
```

---

### Problem 5: Custom Headers
Make a request with custom headers.

```python
import requests

headers = {'User-Agent': 'MyApp/1.0'}
response = requests.get('https://jsonplaceholder.typicode.com/users', headers=headers)

# Your code here
```

---

## 🟡 Intermediate Problems

### Problem 6: Error Handling
Make requests with proper error handling.

```python
import requests

try:
    # Your code here
except requests.exceptions.RequestException as e:
    # Your code here
```

---

### Problem 7: Multiple Requests with Session
Use session to make multiple requests efficiently.

```python
import requests

session = requests.Session()

# Your code here
```

---

### Problem 8: API Data Collection
Collect data from multiple API endpoints and store in a list.

```python
import requests

# Get posts from users 1-3
posts = []
for user_id in range(1, 4):
    # Your code here

print(posts)
```

---

### Problem 9: Pagination Handling
Handle paginated API responses.

```python
import requests

def get_paginated_data(url, page_size=10):
    # Your code here
    pass

all_posts = get_paginated_data('https://jsonplaceholder.typicode.com/posts')
```

---

### Problem 10: Filter and Process Data
Fetch data from API and filter based on conditions.

```python
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = response.json()

# Filter posts by userId
# Your code here
```

---

## 🔴 Advanced Problems

### Problem 11: Weather API Integration
Fetch weather data from OpenWeatherMap API.

```python
import requests

API_KEY = 'YOUR_API_KEY'
city = 'London'

# Your code here
```

---

### Problem 12: GitHub API Integration
Fetch GitHub user repositories and analyze them.

```python
import requests

username = 'octocat'

# Your code here
```

---

### Problem 13: Data Aggregation from Multiple APIs
Combine data from multiple APIs.

```python
import requests

# Your code here
```

---

### Problem 14: Caching API Responses
Implement caching to avoid redundant API calls.

```python
import requests
import json
from datetime import datetime, timedelta

class APICache:
    # Your code here
    pass
```

---

### Problem 15: Rate Limiting
Implement rate limiting for API calls.

```python
import requests
import time

def rate_limited_requests(urls, delay=1):
    # Your code here
    pass
```

---

## Solutions

Check the `solutions.py` file for detailed solutions.
