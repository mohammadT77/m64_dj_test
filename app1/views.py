from django.shortcuts import render, HttpResponse


# Create your views here.

def hello_world_view_func(request):
    return HttpResponse("Hello world!")


def asqar_view_func(request):
    return HttpResponse("Hello asqar!")


def akbar_view_func(request):
    return HttpResponse("Hello akbar!")


def reza_view_func(request):
    return HttpResponse("Hello reza!")
