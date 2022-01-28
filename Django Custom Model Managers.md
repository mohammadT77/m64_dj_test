# Maktab 52 - Django
## Custom model Managers
by: MohammadAmin H.B. Tehrani

----
### Introduction 
A Manager is the interface through which database query operations are provided to Django models. At least one Manager exists for every model in a Django application.  
You can use a custom Manager in a particular model by extending `django.db.Manager` class and instantiating your custom Manager in your model.

```python
from django.db import models

class MyManager(models.Manager):
    pass
```

Now, you can add your own methods into the manager or simply override manager existing methods.

For Example:
1. Writing **MyManager** class:
```python
from django.db import models

class MyManager(models.Manager):
    def some_method(self):
        ...
        return ... 
```

2. Setting `Model.objects`:
```python
class MyModel(models):
    ...
    
    objects = MyManager()
    
```

3. Use new manager:
```python
MyModel.objects.some_method()
```

### Full example: Writing BaseModel

```python

from django.db import models


class BaseManager(models.Manager):
 
    def get_queryset(self):
        """
        Return a new QuerySet object. Subclasses can override this method to
        customize the behavior of the Manager.
        :rtype: QuerySet : Contains only undeleted results.
        """
        # Exclude logically deleted objects ( or filter(deleted=False) ):
        return super().get_queryset().exclude(deleted=True)  # Contains Only UnDeleted records.  

    
    def archive(self):
        """
        This method returns a Django QuerySet contains ALL db records. 
        :rtype: QuerySet : Contains deleted or undeleted results.
        """
        return super().get_queryset()



class BaseModel(models.Model):
    deleted = models.BooleanField(default=False, null=False, blank=False)
    
    class Meta:
        abstract = True  # BaseModel is an Abstract model

    objects = BaseManager()
```




