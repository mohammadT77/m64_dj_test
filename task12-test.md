# Django
## Maktab 64 | Task 12
### Test

----
**A. Model unit tests**   
In this task we're going to write TestCases for `Receipt` model:
  
First, write a proper test methods for:
1. `Receipt.final_price(self)` method.  
This method returns the discounted receipt's total price minus `offcode` discount  
   (Receipt Total Price: Sum of orders final price)  

**_Write at least 5 test methods._**    

Note: Seek to maximize test coverage by writing more test methods.  
For example, Check out all the following scenarios for `Receipt.final_price(self)`:
1. Discount value greater than price
2. Empty discount or with an amount of zero.
3. Without OffCode
4. ...

Then, start implementing the `Reciept.final_price(self)` method.

Hint: You can implement a `BaseDiscount` model inherited with both `Discount` and `OffCode` model, since the methods and functionalities are similar.


**B. View unit tests**  
Write a `RecieptDetailViewTest` method, and check that all the following details are available for clients:
1. List of the receipt's orders
2. Final price
3. Total price
4. ...


**C. Selenium Live Test (Optional)**  
Use selenium in order to test your methods.