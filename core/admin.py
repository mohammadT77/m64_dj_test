from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from core.models import Brand, User

UserAdmin.list_display = ('phone', 'email', 'first_name', 'last_name', 'is_staff')
UserAdmin.search_fields = ('phone', 'first_name', 'last_name', 'email')
UserAdmin.ordering = ('phone',)
UserAdmin.fieldsets[0][1]['fields'] =  ('phone', 'password')

admin.site.register(Brand)
admin.site.register(User, UserAdmin)