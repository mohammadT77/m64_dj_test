# Django
## Maktab 64 | Task 3
### Cafe project: Model - advance

---
**A.** Implement a **abstract** model named `TimestampMixin` that contains 3 useful timestamp attributes:
1. Create timestamp: auto_now_add=True
2. Modify timestamp: auto_now=True
3. Delete timestamp: default=None, null=True, blank=True (useful on logical delete)

Then write a method, `Timestamp.logical_delete(self)`, into the `TimestampMixin` that simulates the object deletion by setting the `delete_timestamp`.


**B.** Implement `Cashier` model that extends from django built-in `User` and `TimestampMixin`  
Then add some extra attributes: 
1. Phone number
2. National code
3. Address

