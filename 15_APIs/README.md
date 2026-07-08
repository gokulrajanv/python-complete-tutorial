# 15. APIs

## Overview
APIs (Application Programming Interfaces) allow different applications to communicate with each other. This section covers REST API basics, the requests library, and API integration.

## Table of Contents
1. [REST API Basics](#rest-api-basics)
2. [requests Library](#requests-library)
3. [API Integration](#api-integration)

---

## REST API Basics

### What is an API?
An API is a set of rules and protocols that allows different software applications to communicate with each other.

### REST (Representational State Transfer)
REST is an architectural style for designing networked applications using HTTP requests.

### HTTP Methods
- **GET**: Retrieve data
- **POST**: Create new data
- **PUT**: Update existing data
- **DELETE**: Delete data
- **PATCH**: Partially update data

### API Endpoints
An endpoint is a specific URL where an API service is hosted.

```
https://api.example.com/v1/users
https://api.example.com/v1/users/123
https://api.example.com/v1/users/123/posts
```

### HTTP Status Codes
- **200-299**: Success
  - 200: OK
  - 201: Created
  - 204: No Content
- **300-399**: Redirection
  - 301: Moved Permanently
  - 304: Not Modified
- **400-499**: Client Error
  - 400: Bad Request
  - 401: Unauthorized
  - 403: Forbidden
  - 404: Not Found
- **500-599**: Server Error
  - 500: Internal Server Error
  - 503: Service Unavailable

### Request and Response Structure

**Request:**
```
GET /users/123 HTTP/1.1
Host: api.example.com
Authorization: Bearer token123
Content-Type: application/json
```

**Response:**
```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com"
}
```

---

## requests Library

### Installation
```bash
pip install requests
```

### Basic Requests

#### GET Request
```python
import requests

# Simple GET request
response = requests.get('https://api.github.com/users/github')

# Check status code
print(response.status_code)  # 200

# Get response text
print(response.text)

# Get response as JSON
data = response.json()
print(data['name'])

# Get response headers
print(response.headers)
```

#### GET Request with Parameters
```python
import requests

# URL parameters
params = {
    'q': 'python',
    'sort': 'stars',
    'per_page': 10
}

response = requests.get('https://api.github.com/search/repositories', params=params)
print(response.url)  # URL with parameters
data = response.json()
print(f"Found {data['total_count']} repositories")
```

#### POST Request
```python
import requests

# POST request with JSON data
data = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'age': 30
}

response = requests.post('https://jsonplaceholder.typicode.com/users', json=data)
print(response.status_code)
print(response.json())
```

#### POST Request with Form Data
```python
import requests

# POST request with form data
data = {
    'username': 'john',
    'password': 'secret123'
}

response = requests.post('https://example.com/login', data=data)
```

#### PUT Request
```python
import requests

# Update existing resource
data = {
    'name': 'Jane Doe',
    'email': 'jane@example.com'
}

response = requests.put('https://jsonplaceholder.typicode.com/users/1', json=data)
print(response.json())
```

#### DELETE Request
```python
import requests

# Delete resource
response = requests.delete('https://jsonplaceholder.typicode.com/users/1')
print(response.status_code)  # 200 if successful
```

### Request Headers
```python
import requests

# Custom headers
headers = {
    'User-Agent': 'My Application',
    'Authorization': 'Bearer your_token_here',
    'Accept': 'application/json'
}

response = requests.get('https://api.github.com/user', headers=headers)
```

### Request Timeout
```python
import requests

# Timeout after 5 seconds
try:
    response = requests.get('https://api.example.com/slow', timeout=5)
except requests.exceptions.Timeout:
    print("Request timed out")
```

### Error Handling
```python
import requests

try:
    response = requests.get('https://api.example.com/endpoint')
    response.raise_for_status()  # Raise exception for bad status codes
    data = response.json()
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.ConnectionError as e:
    print(f"Connection Error: {e}")
except requests.exceptions.Timeout as e:
    print(f"Timeout Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")
```

### Response Properties
```python
import requests

response = requests.get('https://api.github.com/users/github')

# Response content
print(response.status_code)    # Status code
print(response.headers)         # Response headers
print(response.url)             # Actual URL used
print(response.history)         # Redirect history
print(response.encoding)        # Character encoding
print(response.text)            # Response as string
print(response.json())          # Response as JSON
print(response.content)         # Response as bytes
```

---

## API Integration

### Working with JSON APIs
```python
import requests
import json

# Fetch data from API
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
post = response.json()

print(f"Title: {post['title']}")
print(f"Body: {post['body']}")
print(f"User ID: {post['userId']}")
```

### Pagination
```python
import requests

def fetch_all_pages(base_url, per_page=10):
    all_data = []
    page = 1
    
    while True:
        params = {'page': page, 'per_page': per_page}
        response = requests.get(base_url, params=params)
        
        if response.status_code != 200:
            break
        
        data = response.json()
        if not data:
            break
        
        all_data.extend(data)
        page += 1
    
    return all_data

# Fetch all posts
posts = fetch_all_pages('https://jsonplaceholder.typicode.com/posts')
print(f"Total posts: {len(posts)}")
```

### API Authentication
```python
import requests

# Basic Authentication
response = requests.get(
    'https://api.github.com/user',
    auth=('username', 'password')
)

# Token Authentication
headers = {
    'Authorization': 'Bearer your_token_here'
}
response = requests.get('https://api.example.com/endpoint', headers=headers)

# API Key Authentication
params = {
    'api_key': 'your_api_key_here'
}
response = requests.get('https://api.example.com/endpoint', params=params)
```

### Creating a Wrapper Class
```python
import requests
from typing import Dict, Any, Optional

class APIClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            'Content-Type': 'application/json'
        }
        if api_key:
            self.headers['Authorization'] = f'Bearer {api_key}'
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, headers=self.headers, **kwargs)
        response.raise_for_status()
        return response.json()
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        return self._make_request('GET', endpoint, params=params)
    
    def post(self, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        return self._make_request('POST', endpoint, json=data)
    
    def put(self, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        return self._make_request('PUT', endpoint, json=data)
    
    def delete(self, endpoint: str) -> Dict[str, Any]:
        return self._make_request('DELETE', endpoint)

# Using the wrapper
client = APIClient('https://jsonplaceholder.typicode.com')
posts = client.get('/posts')
print(posts)
```

### Rate Limiting
```python
import requests
import time

class RateLimitedClient:
    def __init__(self, base_url: str, requests_per_minute: int = 60):
        self.base_url = base_url
        self.requests_per_minute = requests_per_minute
        self.min_interval = 60 / requests_per_minute
        self.last_request_time = 0
    
    def _wait_for_rate_limit(self):
        elapsed = time.time() - self.last_request_time
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
    
    def get(self, endpoint: str, **kwargs):
        self._wait_for_rate_limit()
        self.last_request_time = time.time()
        response = requests.get(f"{self.base_url}{endpoint}", **kwargs)
        return response.json()

# Using rate-limited client
client = RateLimitedClient('https://api.example.com', requests_per_minute=30)
```

### Caching API Responses
```python
import requests
import json
from datetime import datetime, timedelta

class CachedAPIClient:
    def __init__(self, base_url: str, cache_duration: int = 300):
        self.base_url = base_url
        self.cache = {}
        self.cache_duration = cache_duration
    
    def get(self, endpoint: str, use_cache: bool = True):
        if use_cache and endpoint in self.cache:
            cached_data, timestamp = self.cache[endpoint]
            if datetime.now() - timestamp < timedelta(seconds=self.cache_duration):
                return cached_data
        
        response = requests.get(f"{self.base_url}{endpoint}")
        data = response.json()
        
        self.cache[endpoint] = (data, datetime.now())
        return data

# Using cached client
client = CachedAPIClient('https://jsonplaceholder.typicode.com', cache_duration=600)
posts = client.get('/posts')  # Fetches from API
posts = client.get('/posts')  # Returns cached data
```

---

## Practice Exercises

### Exercise 1: Weather API
Use a weather API to fetch current weather data for different cities and display it.

### Exercise 2: GitHub API
Create a script that searches GitHub repositories and displays results with pagination.

### Exercise 3: Currency Converter
Use a currency conversion API to convert between different currencies.

### Exercise 4: Build a REST API Client
Create a comprehensive API client wrapper for a public API with error handling and caching.

---

## Key Takeaways
✅ REST APIs use HTTP methods (GET, POST, PUT, DELETE)  
✅ Status codes indicate request success or failure  
✅ requests library simplifies HTTP requests  
✅ JSON is the common data format for APIs  
✅ Error handling is crucial for reliability  
✅ Pagination handles large datasets  
✅ Authentication secures API access  

---

## Next Steps
→ Learn about [Testing](../16_Testing/README.md)
