# Django
## Maktab 64 | Task 16
### DRF: Authentication & Permissions

----
**A. Hyperlinked Related Field**    
Use `HyperlinkedRelatedField` for **owner** field into your **Address** serializer.

**B. Pagination**    
Enable `PageNumberPagination` for all your API views.

**C. ViewSet**  
Use `ModelViewSet` class to implement **Order** and **OrderItem** views, like:
- List of Orders
- List of Order Items
- Create new Order
- Create new OrderItems
- Delete Order
- Delete OrderItems
- Modify Order
- Modify OrderItems

**B. Custom template renderer**    
Implement a custom template for the `AddressListAPIView` api view. Then add it in the `AddressListAPIView` renderers.

