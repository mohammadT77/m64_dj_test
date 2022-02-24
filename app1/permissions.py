from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request


class MyCustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.phone.endswith('88')

