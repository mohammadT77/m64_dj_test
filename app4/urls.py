from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('logout/', logout_view, name='logout_view'),
    path('profile/', profile_view, name='profile_view'),
]