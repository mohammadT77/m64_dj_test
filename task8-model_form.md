# Django
## Maktab 64 | Task 8
### Cafe project: MenuItem model-form

----
Like the previous task, Implement the `CreateMenuItem` view, but using **Django Model Forms** instead of Django Forms.  
MenuItem model includes fields like:
- Name: CharField, **MUST BE TITLE** 
- Price: IntegerField, **MUST BE POSITIVE**
- Discount
- Category
- Image
- ...

**Notes:**
- Use Django `ModelForm` class.
- You must save the MenuItem instance into the database.
- You must save the uploaded image in the _MEDIA_ directory.
- You may use generic `FormView`.

