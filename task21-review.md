# Django
## Maktab 64 | Task 21
### Review

----
### A. Back-end: API
1. Use DRF to create the `orderitem_list/<int:order_id>` API:
   - GET: all order items belongs to the order with id = `order_id`
   - POST: create new order item to the order with id = `order_id`
2. Use `BasicAuthentication` as the authentication class of the API view.
3. Add `IsAuthenticated` permission in the API view's permissions
3. Add `IsOwner` permission in the API view's permissions:
   __"The Owner only can add a new order item into his/her orders" BUT "Others can see his/her order items"__
   
### B. Front-end: Ajax/JS
1. Implement a list to show the users' order items (get the order id from a text input)
2. Send a POST request to the API by clicking on a button to add a new order item. 
   
