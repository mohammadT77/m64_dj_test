# Django
## Maktab 64 | Task 16
### DRF: Authentication & Permissions

----
**A. Serializers**    
Implement `AddressSerializer` & `UserSerializer` classes.

**B. Views**
Write views below:
1. **User list view** -> only _permitted_ to superusers.
2. User detail view -> only **_available_** for user him/her self.
3. Address list view -> filtered by the owner
4. Address Detail view -> only _permitted_ to the owner.

**C. Permissions**
Implement the following permissions:
1. IsOwnerPermission
2. IsSuperuserPermission 

**D. Authentication**   
Use BasicAuthentication as your views authentication method