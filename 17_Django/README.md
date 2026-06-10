# 1️⃣7️⃣ Django & Django REST Framework - Complete Guide

Master Django basics, models, views, templates, and REST APIs.

## Table of Contents

1. [Django Basics](#django-basics)
2. [Models](#models)
3. [Views](#views)
4. [Templates](#templates)
5. [Django REST Framework](#django-rest-framework)

---

## 🟡 Django Basics

### Installation

```bash
pip install django
django-admin startproject myproject
cd myproject
python manage.py startapp myapp
```

### Project Structure

```
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    myapp/
        models.py
        views.py
        urls.py
```

---

## 🟡 Models

### Define Model

```python
# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
```

### Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🟡 Views

### Function-Based View

```python
# views.py
from django.shortcuts import render
from .models import User

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/list.html', {'users': users})

def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'users/detail.html', {'user': user})
```

### Class-Based View

```python
from django.views import View
from django.views.generic import ListView, DetailView
from .models import User

class UserListView(ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = User
    template_name = 'users/detail.html'
```

---

## 🟡 Templates

### Template Example

```html
<!-- users/list.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Users</title>
</head>
<body>
    <h1>Users</h1>
    <ul>
    {% for user in users %}
        <li>
            <a href="{% url 'user-detail' user.id %}">{{ user.name }}</a>
            - {{ user.email }}
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```

---

## 🔴 Django REST Framework

### Installation

```bash
pip install djangorestframework
```

### Serializers

```python
# serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'age']
```

### ViewSets

```python
# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

### Routers

```python
# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

### API Endpoints

```
GET    /api/users/           - List all users
POST   /api/users/           - Create user
GET    /api/users/{id}/      - Get user
PUT    /api/users/{id}/      - Update user
DELETE /api/users/{id}/      - Delete user
```

---

## 📝 Summary

| Component | Purpose |
|-----------|---------|
| Models | Database structure |
| Views | Business logic |
| Templates | HTML pages |
| Serializers | JSON conversion |
| ViewSets | API endpoints |
| Routers | URL mapping |

---

**Congratulations! You've completed the entire Python tutorial! 🎉**

Now it's time to build projects and practice! Start with small projects and gradually increase complexity.

Good luck on your Python journey! 🚀
