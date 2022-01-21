from django.urls import path
from .views import *

urlpatterns = [
    path('brand/', create_brand, name='create_brand'),
    path('<str:person_name>/', hello_world_view_func, name="hello"),
    # path('akbar/', akbar_view_func, name="hello_akbar"),
    # path('asqar/', asqar_view_func, name="hello_asqar"),
    # path('reza/', reza_view_func, name="hello_reza"),

    path('car/', get_car, name='get_car', kwargs={'car_id':2}),
    path('car/<int:car_id>/', get_car, name='get_car'),


]