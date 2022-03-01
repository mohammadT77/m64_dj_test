# Maktab 64 - Django
## Custom Middleware
by: MohammadAmin H.B. Tehrani

----

### Introduction

Middleware is a framework of hooks into Django’s request/response processing. It’s a light, low-level “plugin” system for globally altering Django’s input or output.

Each middleware component is responsible for doing some specific function. For example, Django includes a middleware component, AuthenticationMiddleware, that associates users with requests using sessions.

This document explains how middleware works, how you activate middleware, and how to write your own middleware. Django ships with some built-in middleware you can use right out of the box. They’re documented in the built-in middleware reference.

### First
Create `middleware.py` module into your app package:
E.g: `myproject/myapp/middleware.py`

### Writing Function-Based middleware
```python
def custom_func_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
```

### Writing Class-Based middleware

```python
class CustomClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

```

### Activating (Installing) middleware
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'myapp.middleware.CustomClassMiddleware',
    'myapp.middleware.custom_func_middleware',
]
```



### Full document:
https://docs.djangoproject.com/en/3.2/topics/http/middleware/