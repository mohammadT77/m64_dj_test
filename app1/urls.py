from django.urls import path
from .views import *

urlpatterns = [
    path('index/', hello_world_view_func),
    path('akbar/', akbar_view_func),
    path('asqar/', asqar_view_func),
    path('reza/', reza_view_func),
]