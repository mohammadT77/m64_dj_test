from datetime import datetime

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render, HttpResponse, get_object_or_404

# Create your views here.
from django.views import View

from app1.models import Car
from core.models import Brand


def hello_world_view_func(request, person_name):
    brand = Brand.objects.last()
    # brand.car_set!


#
#
# def asqar_view_func(request):
#     return HttpResponse("Hello asqar!")
#
#
# def akbar_view_func(request):
#     return HttpResponse("Hello akbar!")
#
#
# def reza_view_func(request):
#     return HttpResponse("Hello reza!")
#
#
# def get_car(request, car_id):
#     car: Car = get_object_or_404(Car, id=car_id)
#     return render(request, 'app1/car.html', {'car': car})
#
#
# def create_brand(request):
#     if request.method == 'GET':
#         return render(request, 'app1/create_brand.html')
#     elif request.method == 'POST':
#         data = request.POST  # data = {'name': ..., 'country': ... }
#         # validate!!!
#         new_brand = Brand.objects.create(name=data['name'], country=data['country'])
#         return HttpResponse(f"Successfully Created: {new_brand}")
#     else:
#         return HttpResponse("Invalid method!", status=405)
#
#
# # Class-Based views!
# class CreateCar(View):
#
#     def get(self, request):
#         return render(request, 'app1/create_car.html')
#
#     def post(self, request):
#         data = request.POST
#         new_car = Car.objects.create(acceleration=data['acceleration'], color=data['color'], brand_id=data['brand_id'])
#         return HttpResponse(f"Successfully Created: {new_car}")

from django.views import generic


class BrandListView(generic.CreateView):
    model = Brand
    template_name = 'app1/brand_list.html'

    def get_queryset(self):
        req = self.request
        country = req.GET.get('country', None)  # ?country=...
        return Brand.objects.filter(country=country) if country else Brand.objects.all()


# class BrandDetailView(generic.DetailView):
#     model = Brand
#     template_name = 'app1/brand_detail.html'
@permission_required('app1.wash_car')
def test_view(request):
    if request.user.has_perm('app1.add_car'):
        ...
    elif request.user.has_perm('app1.delete_car'):
        ...

    name = request.session.get('name', None)

    if name is not None:
        resp = HttpResponse(f"Hello {name}!")
    else:
        request.session['name'] = 'shayan'  # Session!!
        resp = HttpResponse(f"Hello Unknown!!! Setting session!!!")

    return resp


class TestView(PermissionRequiredMixin, View):
    permission_required = 'app1.wash_car'

    def get(self, request):
        return HttpResponse("Hello Shayan!")
