from django.http import Http404
from django.shortcuts import render, HttpResponse, get_object_or_404

# Create your views here.
from app1.models import Car
from core.models import Brand


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


def create_brand(request):
    if request.method == 'GET':
        return render(request, 'app1/create_brand.html')
    elif request.method == 'POST':
        data = request.POST  # data = {'name': ..., 'country': ... }
        # validate!!!
        new_brand = Brand.objects.create(name=data['name'], country=data['country'])
        return HttpResponse(f"Successfully Created: {new_brand}")
    else:
        return HttpResponse("Invalid method!", status=405)
