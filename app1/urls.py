from django.urls import path
from django.views.generic import DetailView, ListView

from .views import *

urlpatterns = [
    # path('brand/', create_brand, name='create_brand'),
    # path('create_car/', CreateCar.as_view(), name='create_car'),
    #
    # path('<str:person_name>/', hello_world_view_func, name="hello"),
    # path('akbar/', akbar_view_func, name="hello_akbar"),
    # path('asqar/', asqar_view_func, name="hello_asqar"),
    # path('reza/', reza_view_func, name="hello_reza"),

    # path('car/', get_car, name='get_car', kwargs={'car_id':2}),
    # path('car/<int:car_id>/', get_car, name='get_car'),

    path('brand/', ListView.as_view(model=Brand, template_name='app1/brand_list.html'), name='brand_list'),
    path('brand/<int:pk>',
         DetailView.as_view(template_name='app1/brand_detail.html', model=Brand),
         name='brand_detail'),

    path('test/', TestView.as_view(), name='test_View')

]