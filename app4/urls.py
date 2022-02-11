from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordChangeView
from django.urls import path

from .views import *

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login_view'),
    path('logout/', LogoutView.as_view(), name='logout_view'),
    path('register/', register_view, name='register_view'),
    path('profile/', profile_view, name='profile_view'),
    path('password-reset/', PasswordResetView.as_view(), name='passreset_view'),
    path('password-change/', PasswordChangeView.as_view(), name='passchange_view'),
]