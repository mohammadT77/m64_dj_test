from django.urls import path
from django.views.generic import DetailView, ListView

from .views import *

urlpatterns = [
    path('create/', create_message, name='create-message'),
    path('view/', view_message, name='view-message'),

]