# Maktab 52 - Django
## Class-based Views
by: MohammadAmin H.B. Tehrani

----
A view function, or view for short, is a Python function that takes a Web request and returns a Web response. This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really.

**1. Function-based views:**  
  ```python
def example_view(request, *args):
    pass
   ```
<br/>

**2. Class-based views:**
This can be more than just a function, and Django provides an example of some classes which can be used as views. These allow you to structure your views and reuse code by harnessing inheritance and mixins.

**Import:**  
```python
from django.views import View
```
<br/>

**View implementation:**
```python
class LoginView(View):

  # GET method allowed by the function below:
  def get(self, request, *args, **kwargs):
    return ...

  # Also POST method ...
  def post(self, request, *args, **kwargs):
    return ...
```
You should to implement the methods you want to interact with. Otherwise, it is considered as a `NotAllowedMethod`. 
<br/>

**In url.py:**
```python
urlpatterns = [
    path('login/', LoginView.as_view()),
    ...
]
```
<br/>


**Dispatching:**
```python
urlpatterns = [
    path('login/<str:some_thing>', LoginView.as_view()),
    ...
]
```
```python
class LoginView(View):

    # Modifying slugs...  
    def dispatch(self, request, *args, **kwargs):
        kwargs['some_thing'] = ...
        return super().dispatch(request, *args, **kwargs)
    
    # Retrieving data after modifying at the dispatch method. 
    def get(self, request, *args, **kwargs):
        print(kwargs['some_thing'])
        return ...

    # Also Retrieving data ...
    def post(self, request, *args, **kwargs):
        print(kwargs['some_thing'])
        return ...
```
