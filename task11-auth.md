# Django
## Maktab 64 | Task 11
### Authentication

----
Use **django auth Views**, to implement views below same as the previous task:
### A.  Login view
Utilize django auth **LoginView** to implement your website login view.

### B. Profile view
Create a profile view, that shows the user information, 
**if the user is authenticated** and **has `auth.see_profile` permission**, redirect to the **Login page** otherwise.

**Note:** You should create a custom permission `auth.see_profile` initially.

### C. Logout view
Create a logout view, using django auth **LogoutView**.

### D. User registration or Sign Up view (Optional)
Create a user registration view, to sign up users.  
**Note:** You may use ModelForms to simplify implementation.
