# 1️⃣5️⃣ APIs - Complete Guide

Master REST API Basics, requests library, and API integration.

## Table of Contents

1. [REST API Basics](#rest-api-basics)
2. [requests Library](#requests-library)
3. [HTTP Methods](#http-methods)
4. [Headers & Authentication](#headers--authentication)
5. [API Integration](#api-integration)

---

## 🟢 REST API Basics

### What is a REST API?

REST (Representational State Transfer) is an architectural style for web APIs.

### Key Concepts

- **Resource**: Data object (User, Post, etc.)
- **Endpoint**: URL to access a resource
- **HTTP Methods**: GET, POST, PUT, DELETE, PATCH
- **Status Codes**: 200, 201, 400, 401, 404, 500, etc.

### HTTP Status Codes

```
2xx - Success
200 - OK
201 - Created

3xx - Redirection
301 - Moved Permanently
302 - Found

4xx - Client Error
400 - Bad Request
401 - Unauthorized
403 - Forbidden
404 - Not Found

5xx - Server Error
500 - Internal Server Error
503 - Service Unavailable
```

---

## 🟢 requests Library

### Installation

```bash
pip install requests
```

### Basic GET Request

```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # 200
print(response.json())       # Response as JSON
```

### Accessing Response Data

```python
response = requests.get('https://api.github.com/users/github')

print(response.status_code)  # Status code
print(response.text)         # Response body as string
print(response.json())       # Response body as JSON
print(response.headers)      # Response headers
print(response.url)          # Final URL
```

---

## 🟡 HTTP Methods

### GET Request

```python
import requests

# Simple GET
response = requests.get('https://api.github.com/users/octocat')
print(response.json())

# GET with query parameters
params = {'page': 1, 'per_page': 10}
response = requests.get('https://api.github.com/users', params=params)
```

### POST Request

```python
import requests

# POST with JSON data
data = {
    'name': 'John Doe',
    'email': 'john@example.com'
}
response = requests.post('https://api.example.com/users', json=data)
print(response.status_code)
print(response.json())
```

### PUT Request

```python
import requests

# Update entire resource
data = {
    'name': 'Jane Doe',
    'email': 'jane@example.com'
}
response = requests.put('https://api.example.com/users/1', json=data)
```

### PATCH Request

```python
import requests

# Partial update
data = {'name': 'Jane Doe'}
response = requests.patch('https://api.example.com/users/1', json=data)
```

### DELETE Request

```python
import requests

# Delete resource
response = requests.delete('https://api.example.com/users/1')
print(response.status_code)  # 204 (No Content)
```

---

## 🟡 Headers & Authentication

### Custom Headers

```python
import requests

headers = {
    'User-Agent': 'MyApp/1.0',
    'Content-Type': 'application/json'
}
response = requests.get('https://api.example.com/data', headers=headers)
```

### Basic Authentication

```python
import requests
from requests.auth import HTTPBasicAuth

# Method 1
response = requests.get('https://api.example.com/data',
                       auth=('username', 'password'))

# Method 2
response = requests.get('https://api.example.com/data',
                       auth=HTTPBasicAuth('username', 'password'))
```

### Bearer Token Authentication

```python
import requests

headers = {
    'Authorization': 'Bearer YOUR_TOKEN_HERE'
}
response = requests.get('https://api.example.com/data', headers=headers)
```

### API Key Authentication

```python
import requests

params = {'api_key': 'YOUR_API_KEY'}
response = requests.get('https://api.example.com/data', params=params)
```

---

## 🟡 API Integration

### Error Handling

```python
import requests

try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()  # Raise exception for bad status
    data = response.json()
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")
```

### Timeout

```python
import requests

try:
    response = requests.get('https://api.example.com/data', timeout=5)
except requests.exceptions.Timeout:
    print("Request timed out")
```

### Session for Multiple Requests

```python
import requests

session = requests.Session()
session.headers.update({'Authorization': 'Bearer TOKEN'})

# Use session for multiple requests
response1 = session.get('https://api.example.com/users')
response2 = session.get('https://api.example.com/posts')
```

### Pagination

```python
import requests

def get_all_pages(url):
    all_data = []
    page = 1
    
    while True:
        response = requests.get(url, params={'page': page})
        if response.status_code != 200:
            break
        
        data = response.json()
        if not data:
            break
        
        all_data.extend(data)
        page += 1
    
    return all_data
```

### Rate Limiting

```python
import requests
import time

def make_request_with_limit(url, delay=1):
    try:
        response = requests.get(url)
        response.raise_for_status()
        time.sleep(delay)  # Wait before next request
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
```

### JSON Processing

```python
import requests
import json

# Get data from API
response = requests.get('https://api.github.com/users/octocat')
user_data = response.json()

print(json.dumps(user_data, indent=2))
```

---

## 📝 Summary

| Method | Purpose | Status |
|--------|---------|--------|
| GET | Retrieve data | 200 |
| POST | Create new resource | 201 |
| PUT | Replace resource | 200 |
| PATCH | Partial update | 200 |
| DELETE | Remove resource | 204 |

---

**Next:** [16_Testing](../16_Testing/README.md) →
