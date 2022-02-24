from datetime import datetime

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import Http404, JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from app1.models import Car, Address
from app1.serializers import CarSerializer, BrandSerializer, AddressSerializer
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


@csrf_exempt
def car_list_api(request):
    """
    POST: create Car
    GET: List Cars
    :param request:
    """

    if request.method == 'GET':
        car_serializer = CarSerializer(Car.objects.all(), many=True)
        return JsonResponse({'data': car_serializer.data}, status=200)
    elif request.method == 'POST':
        data = request.POST
        car_serializer = CarSerializer(data=data)
        if car_serializer.is_valid():
            new_car = car_serializer.save()
            return JsonResponse({'new_car_id': new_car.id}, status=201)
        else:
            return JsonResponse({'errors': car_serializer.errors}, status=400)
    else:
        return JsonResponse({}, status=405)


from rest_framework.decorators import api_view
from rest_framework import generics


class BrandListApi(generics.ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


from rest_framework import mixins, generics, authentication
from .permissions import MyCustomPermission


# GET: Detail brand, PUT: update (complete), PATCH: partial update!, DELETE: delete!
class BrandDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.TokenAuthentication]


# class BrandDetailApi(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
#                      generics.GenericAPIView):
#
#     serializer_class = BrandSerializer
#     queryset = Brand.objects.all()
#
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
@api_view(['GET'])
def car_detail(request, pk):
    car_ins = Car.objects.get(id=pk)
    car_serializer = CarSerializer(car_ins, context={'request': request})
    return Response(car_serializer.data)


from rest_framework import renderers

class AddressListApi(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    template_name = 'address_list.html'
