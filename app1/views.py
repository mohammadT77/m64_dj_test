from django.http import Http404
from django.shortcuts import render, HttpResponse, get_object_or_404

# Create your views here.
from app1.models import Car


def hello_world_view_func(request, person_name):
    if person_name == 'akbar':
        raise Http404()
    return render(request, 'app1/index.html', {'pname': person_name})


def asqar_view_func(request):
    return HttpResponse("Hello asqar!")


def akbar_view_func(request):
    return HttpResponse("Hello akbar!")


def reza_view_func(request):
    return HttpResponse("Hello reza!")


def get_car(request, car_id):
    car: Car = get_object_or_404(Car, id=car_id)
    return render(request, 'app1/car.html', {'car': car})
