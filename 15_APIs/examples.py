# ===================================
# 15 - APIs Examples
# ===================================

import requests
import json

print("\n=== API EXAMPLES ===")

# ===== BASIC GET REQUEST =====
print("\n--- Basic GET Request ---")
try:
    response = requests.get('https://api.github.com')
    print(f"Status Code: {response.status_code}")
    print(f"Headers: {dict(list(response.headers.items())[:3])}")
except Exception as e:
    print(f"Error: {e}")

# ===== GET WITH PARAMETERS =====
print("\n--- GET with Parameters ---")
try:
    params = {'q': 'python', 'sort': 'stars'}
    response = requests.get('https://api.github.com/search/repositories',
                          params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"Total results: {data.get('total_count')}")
        if data.get('items'):
            print(f"First result: {data['items'][0].get('name')}")
except Exception as e:
    print(f"Error: {e}")

# ===== ERROR HANDLING =====
print("\n--- Error Handling ---")
try:
    response = requests.get('https://api.github.com/users/octocat')
    response.raise_for_status()  # Raise exception for bad status
    data = response.json()
    print(f"User: {data.get('login')}")
    print(f"Name: {data.get('name')}")
    print(f"Location: {data.get('location')}")
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")

# ===== CUSTOM HEADERS =====
print("\n--- Custom Headers ---")
try:
    headers = {
        'User-Agent': 'Python-Requests/Tutorial'
    }
    response = requests.get('https://api.github.com/rate_limit', headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"Rate Limit Info: {data.get('rate_limit', {}).get('limit')}")
except Exception as e:
    print(f"Error: {e}")

# ===== JSON RESPONSE PROCESSING =====
print("\n--- JSON Response Processing ---")
try:
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    if response.status_code == 200:
        todo = response.json()
        print(f"Todo: {todo.get('title')}")
        print(f"Completed: {todo.get('completed')}")
        print(f"JSON Response:\n{json.dumps(todo, indent=2)}")
except Exception as e:
    print(f"Error: {e}")

# ===== MULTIPLE REQUESTS =====
print("\n--- Multiple Requests (with Session) ---")
try:
    session = requests.Session()
    
    # Get multiple todos
    for todo_id in range(1, 4):
        response = session.get(f'https://jsonplaceholder.typicode.com/todos/{todo_id}')
        if response.status_code == 200:
            todo = response.json()
            print(f"{todo_id}. {todo.get('title')}")
except Exception as e:
    print(f"Error: {e}")

print("\nDone!")
